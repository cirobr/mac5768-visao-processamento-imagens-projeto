import numpy as np
from skimage import io
import pandas as pd
import matplotlib.pyplot as plt

# ler datasets
p1 = "./averageGrayDataset/"
m1 = "grade.csv"
f1 = p1 + m1
df1 = pd.read_csv(f1, sep=";")

p2 = "./averageNormalizedGrayDataset/"

# lista de classes
#classes = ["garfo", "faca", "colher", "copo", "caneca", "alicate", "chave", "caneta", "livro", "caderno"]

# varredura de fotos por classes
for ind in df1.index:
    
    # ler fotos e calcular histogramas
    fx1 = p1 + df1.arquivo[ind]
    img1 = io.imread(fx1)
    
    fx2 = p2 + df1.arquivo[ind]
    img2 = io.imread(fx2)

    # plotagem "mnist-like"
    plt.close("all")
    f = plt.figure(figsize=(10,10))
    ax = np.zeros((2,2), dtype=np.object)
    f.suptitle('Protótipo Médio e Histograma: Classe = ' + df1.tipo_obj[ind], fontsize=22)
    
    ax[0,0] = plt.subplot(2, 2, 1)
    ax[0,1] = plt.subplot(2, 2, 2)
    ax[1,0] = plt.subplot(2, 2, 3)
    ax[1,1] = plt.subplot(2, 2, 4)

    ax[0, 0].set_title(p1)
    ax[0, 1].set_title(p2)
    
    ax[0, 0].set(xticks=[], yticks=[])
    ax[0, 0].imshow(img1, cmap='gray', vmin=0, vmax=255)
    ax[0, 1].set(xticks=[], yticks=[])
    ax[0, 1].imshow(img2, cmap='gray', vmin=0, vmax=255)

    h1 = ax[1, 0].hist(img1.ravel(), np.linspace(0, 255, 256))
    h2 = ax[1, 1].hist(img2.ravel(), np.linspace(0, 255, 256))

    plt.tight_layout()
    io.show()

    # roda o loop apenas uma vez
    #break
