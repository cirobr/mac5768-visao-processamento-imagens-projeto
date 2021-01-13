from time import time
import pandas as pd
from skimage import io
import matplotlib.pyplot as plt
from cv2 import resize

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
for foto in df1["arquivo"]:
    fullname1 = pasta1 + foto
    img1 = io.imread(fullname1)
    fotos1.append(img1)

    
# normalizar fotos para dimensão máxima do bbox
d = 100
dim = (d, d)
fotos2 = [resize(img1, dim) for img1 in fotos1]      # a normalização está sendo feita de forma desproporcional


# criar arrays de predictors e outcomes
X = [f2.flatten() for f2 in fotos2]
y = df1["objeto"]

"""
# plotagem de fotos
plt.close("all")
for ind in range(len(fotos1)):
    f, ax = plt.subplots(1, 2, figsize=(10, 10))
    #x = 10
    ax[0].set_title("Classe: " + y[ind])
    ax[0].imshow(fotos1[ind], cmap=plt.cm.gray)
    ax[0].set(xticks=[], yticks=[])
    ax[1].imshow(fotos2[ind], cmap=plt.cm.gray)
    ax[1].set(xticks=[], yticks=[])

    plt.tight_layout()
    io.show()
    #break
"""

### dividir os dados em trainset e testset
###
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.25,
                                                    random_state=42)

### calcular PCA
###
n_components = 45

print("PCA - Extracting eigenvectors")
t0 = time()

pca = PCA(n_components=n_components,
          svd_solver='randomized',
          whiten=True).fit(X_train)
print("done in %0.3fs" % (time() - t0))

eigenfaces = pca.components_.reshape((n_components, d, d))  ### verificar valor para d
print("PCA - Projecting to new orthonormal coordinates")
t0 = time()

X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)
print("done in %0.3fs" % (time() - t0))


### treinar o modelo com SVM
###
print("SVM - Fitting the classifier to the training set")
t0 = time()

param_grid = {'C': [1e3, 5e3, 1e4, 5e4, 1e5],
              'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1], }
clf = GridSearchCV(SVC(kernel='rbf',
                       class_weight='balanced'),
                   param_grid)
clf = clf.fit(X_train_pca, y_train)

print("done in %0.3fs" % (time() - t0))
print("Best estimator found by grid search:")
print(clf.best_estimator_)


### avaliar o modelo com o trainset
###
print("Predicting classes on the train set")
t0 = time()
y_pred = clf.predict(X_train_pca)
print("done in %0.3fs" % (time() - t0))

print(classification_report(y_train, y_pred))
print(confusion_matrix(y_train, y_pred))


### avaliar o modelo com o testset
###
print("Predicting classes on the test set")
t0 = time()
y_pred = clf.predict(X_test_pca)
print("done in %0.3fs" % (time() - t0))

print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
