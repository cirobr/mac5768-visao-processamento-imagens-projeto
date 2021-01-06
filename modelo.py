import numpy as np
import pandas as pd
from skimage import io
from cv2 import resize
import matplotlib.pyplot as plt



# ler metadados segmentação manual
pasta1 = "./bboxManual/"
metafile1 = "grade.csv"
filename1 = pasta1 + metafile1
df1 = pd.read_csv(filename1, sep=";")
print(df1.head(5), "\n")

# ler fotos em uma lista
fotos1 = []
max_r = 0
max_c = 0
for foto in df1["arquivo"]:
    fullname1 = pasta1 + foto
    img1 = io.imread(fullname1)
    fotos1.append(img1)
    
    # determinar dimensões máximas das imagens
    if img1.shape[0] > max_r:
        max_r = img1.shape[0]
    if img1.shape[1] > max_c:
        max_c = img1.shape[1]

    #break
new_dim = (max_r, max_c)

# normalizar fotos para dimensões máximas
img2 = resize(img1, new_dim)
# plotagem de fotos identificadas
plt.close("all")
f, ax = plt.subplots(1, 2, figsize=(10, 10))
ax[0].imshow(img1, cmap=plt.cm.gray)
ax[0].set(xticks=[], yticks=[])
ax[1].imshow(img2, cmap=plt.cm.gray)
ax[1].set(xticks=[], yticks=[])

plt.tight_layout()
io.show()



# criar arrays de predictors e outcomes




# dividir os dados em trainset e testset




# calcular PCA




# treinar o modelo com SVM




# avaliar o modelo com o testset




