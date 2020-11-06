# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 00:43:17 2020

@author: ciror
"""

#import numpy as np
#from scipy.signal import convolve2d as conv2
from skimage import io
from skimage.color import rgb2gray
import pandas as pd

# arquivo de metadados em cores
pasta = "./fotos-teste/"
metafile = "grade_fotos.csv"
filename = pasta + metafile
df = pd.read_csv(filename, sep=";")
print(df.head(5), "\n")

# arquivo de metadados em cinza
pasta2 = pasta
metafile2 = "grade_cinza.csv"
filename2 = pasta2 + metafile2

# quantidade de fotos
n = len(df.arquivo)

# criar dataframe vazio para metadados em cinza
df2 = pd.DataFrame(data=None, columns=df.columns)
df2.insert(loc=5, column="transformacao", value=[])
df2_length = len(df2)

# transformação de fotos cinza
fotos = []
gray_fotos = []
for ind in df.index:
    # ler foto colorida para a lista
    #print(df.loc[ind])
    arq = df["arquivo"][ind]
    filename = pasta + arq
    fotos.append(io.imread(filename))
    
    # gerar foto cinza
    img_gray = rgb2gray(fotos[-1])
    gray_fotos.append(img_gray)
     
    # nome do arquivo da foto cinza
    arq1 = int(arq[:-4])
    arq2 = arq1 + n
    arq2 = str(arq2) + ".jpg"
     
    # gravar dados da foto cinza no dataframe
    l = [df.sequencia[ind], df.objeto[ind], df.tipo_obj[ind], df.fundo[ind], df.iluminacao[ind], "cinza", df.responsavel[ind], arq2]
    df2.loc[df2_length] = l
    df2_length += 1

# salvar metadados em cinza
print(df2.head(5), "\n")
df2.to_csv(filename2, index = False, header=True, sep=";")

# salvar fotos cinza
for ind in df2.index:
    arq = df2["arquivo"][ind]
    filename2 = pasta2 + arq
    
    io.imsave(filename2, gray_fotos[ind])
