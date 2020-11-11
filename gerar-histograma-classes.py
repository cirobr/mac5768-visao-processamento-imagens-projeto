import numpy as np
from skimage import io
import pandas as pd
import matplotlib.pyplot as plt

# adequação do nome de arquivo nos metadados
def fix_jpeg_name(arq):
    arq2 = int(arq[:-4])
    arq2 = str(arq2) + ".jpg"
    return arq2


# ler arquivo de metadados aumentados
pasta = "./augmentedDataset/"
metafile = "grade-augmented.csv"
filename = pasta + metafile
df = pd.read_csv(filename, sep=";")

# dimensões das fotos
s = [(3096, 4128), (2608, 4640)]

# lista de classes
classes = ["garfo", "faca", "colher", "copo", "caneca", "alicate", "chave", "caneta", "livro", "caderno"]

# varredura de fotos por classes
for i in range(len(classes)):

    # filtrar df para a classe sob análise
    df2 = df[df.objeto == classes[i]]
    print(df2.head(5), "\n")
    
    # criar matriz de soma de fotos
    I0 = np.zeros(s[0])
    I1 = np.zeros(s[1])

    # calcular foto média
    n = 0
    for arq in df2.arquivo:
        arq = fix_jpeg_name(arq)
        f = pasta + arq
        img = io.imread(f)
        n += 1

        if img.shape not in s:
            img = np.transpose(img)

        if img.shape == s[0]:
            I0 = I0 + img
        else:
            I1 = I1 + img

    if np.all(np.equal(I1, 0)):
        Im = np.divide(I0, n)
    else:
        Im = np.divide(I1, n)

    Im = Im.astype(np.uint8)
   
    # apresentar Im
    io.imshow(Im)
    io.show()
    
    # apresentar histograma
    plt.hist(Im.ravel(), np.linspace(0, 255, 256))
    plt.show()

    # roda o loop apenas uma vez
    #break