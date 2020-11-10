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
pasta = "./originalDataset/"
metafile = "grade-fotos.csv"
filename = pasta + metafile
df = pd.read_csv(filename, sep=";")

# lista de classes
classes = ["garfo", "faca", "colher", "copo", "caneca", "alicate", "chave", "caneta", "livro", "caderno"]

# filtrar um objeto representativo por classe
seq = "1"
tipo = "a"
fundo = "branco"
ilum = "indoor dia"

#df2 = df[df.sequencia == seq, df.tipo_obj == tipo, df.fundo == fundo, df.iluminacao == ilum]
df2 = df[df.sequencia == seq]
print(df2.head(5), "\n")
