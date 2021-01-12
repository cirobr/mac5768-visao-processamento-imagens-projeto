import pandas as pd
from skimage import io
from cv2 import resize
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix


# ler metadados segmentação manual
pasta1 = "./bboxManual/"
metafile1 = "grade.csv"
filename1 = pasta1 + metafile1
df1 = pd.read_csv(filename1, sep=";")
print(df1.head(5), "\n")


# ler fotos em uma lista
fotos1 = []
#max_r = 0
#max_c = 0
for foto in df1["arquivo"]:
    fullname1 = pasta1 + foto
    img1 = io.imread(fullname1)
    fotos1.append(img1)
    
d = 100
dim = (d, d)

# normalizar fotos para dimensão máxima do bbox
fotos2 = [resize(img1, dim) for img1 in fotos1]      # a normalização está sendo feita de forma desproporcional

"""
###
### plotagem do resize
###
plt.close("all")
f, ax = plt.subplots(1, 2, figsize=(10, 10))
x = 10
ax[0].imshow(fotos1[x], cmap=plt.cm.gray)
ax[0].set(xticks=[], yticks=[])
ax[1].imshow(fotos2[x], cmap=plt.cm.gray)
ax[1].set(xticks=[], yticks=[])

plt.tight_layout()
io.show()
"""

### criar arrays de predictors e outcomes
###
X = [f2.flatten() for f2 in fotos2]
y = df1["objeto"]


### dividir os dados em trainset e testset
###
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.25,
                                                    random_state=42)

### calcular PCA
###
n_components = 45

pca = PCA(n_components=n_components,
          svd_solver='randomized',
          whiten=True).fit(X_train)

eigenfaces = pca.components_.reshape((n_components, d, d))

X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)


### treinar o modelo com SVM
###
param_grid = {'C': [1e3, 5e3, 1e4, 5e4, 1e5],
              'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1], }
clf = GridSearchCV(SVC(kernel='rbf',
                       class_weight='balanced'),
                   param_grid)
clf = clf.fit(X_train_pca, y_train)
print("Best estimator found by grid search:")
print(clf.best_estimator_)


### avaliar o modelo com o testset
###
y_pred = clf.predict(X_test_pca)
