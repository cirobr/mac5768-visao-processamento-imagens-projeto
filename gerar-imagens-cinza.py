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

# leitura dos metadados em cores
pasta = "./fotos-teste/"
metafile = "grade_fotos.csv"
filename = pasta + metafile
df = pd.read_csv(filename, sep=";")
print(df.head(5), "\n")

# gravação das imagens em cinza
pasta2 = pasta
metafile2 = "grade_cinza.csv"
filename2 = pasta2 + metafile2

# quantidade de fotos
n = len(df.arquivo)

# criar dataframe para metadados em cinza
df2 = pd.DataFrame(index=df.index,columns=df.columns)

fotos = []
gray_fotos = []
for f in df:
    print(f)
    filename = pasta + f.arquivo
    fotos.append(io.imread(filename))
    
    # fotos cinza
    img_gray = rgb2gray(fotos[-1])
    gray_fotos.append(img_gray)
     
    # nome do arquivo da foto cinza
    old_f = int(f[:-4])
    new_f = old_f + n
    new_f = str(new_f) + ".jpg"
    
    # gravar dados no dataframe cinza
    l = [f.sequencia, f.objeto, f.tipo_obj, f.fundo, f.iluminacao, f.responsavel, new_f]
    df2_length = len(df2)
    df2.loc[df2_length] = l