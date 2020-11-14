import os
#import numpy as np
from skimage import io
from skimage import exposure
from skimage.util import img_as_ubyte
import pandas as pd


# arquivo de entrada em cinza
pasta1 = "augmentedDataset"
metafile1 = "grade-augmented.csv"
filename1 = pasta1 + "/" + metafile1

lista_fotos = os.listdir(pasta1)

# arquivo de saída normalizada
pasta2 = "normalizedAugmentedDataset"
metafile2 = "grade-augmented-normalized.csv"
filename2 = pasta2 + "/" + metafile2

# normalização de fotos
lista_fotos = os.listdir(pasta1)
for nome_foto in lista_fotos:
    
    if ".csv" in nome_foto:
        continue

    fullname1 = pasta1 + '/' + nome_foto
    img = io.imread(fullname1)
    img_norm = exposure.equalize_hist(img, nbins = 256)
    img_norm2 = img_as_ubyte(img_norm)
    
    # salvar foto gerada
    fullname2 = pasta2 + '/' + nome_foto
    io.imsave(fullname2, img_norm2)

    # roda o loop apenas uma vez
    #break
    
# gerar metadados normalizados
df = pd.read_csv(filename1, sep=";")
print(df.head(5), "\n")

df2 = pd.DataFrame(df)
for ind in df2.index:
    df2.transformacao = "normalized augmented"
print(df2.head(5), "\n")
df2.to_csv(filename2, index = False, header=True, sep=";")

