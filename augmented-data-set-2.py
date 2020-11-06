# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 00:43:17 2020

@author: ciror
"""

import numpy as np
from scipy.signal import convolve2d as conv2
from skimage import io
from skimage.color import rgb2gray
import pandas as pd

# definição de funções de transformação
def transf_grad(img):
    img_aux = np.gradient(img)
    img2 = np.sqrt(np.square(img_aux[0]) + np.square(img_aux[1]))
    return img2

def transf_log2(img, c):
    img2 = c * np.log2(1 + img)
    return img2

def transf_gama(img, c, gama):
    img2 = c * np.power(img, gama)
    return img2

# leitura dos metadados
pasta = "./fotos-teste/"
metafile = "grade_fotos.csv"
filename = pasta + metafile
df = pd.read_csv(filename, sep=";")
print(df, "\n")

# filtragem de dados
df2 = df[(df["objeto"] == "copo")]
print(df2, "\n")

cat = ["caneca", "alicate"]

for c in cat:
    df2 = df[(df["objeto"] == c)]

    fotos = []
    for f in df2.arquivo:
        filename = pasta + f
        fotos.append(io.imread(filename))
   
    for img in fotos:
        # foto original
        io.imshow(img)
        io.show()
    
        # foto cinza
        img_gray = rgb2gray(img)
        io.imshow(img_gray)
        io.show()
    
        # soma de fundo (gradiente) com foto cinza
        img_grad = transf_grad(img_gray)
        io.imshow(img_grad)
        io.show()
        # compor imagem cinza com gradiente
        img_gray_grad = img_gray + img_grad
        io.imshow(img_gray_grad)
        io.show()
    
        # foto log2
        img_log2 = transf_log2(img_gray, c = 1)
        io.imshow(img_log2)
        io.show()
    
        # foto exponencial
        img_gama = transf_gama(img_gray, c = 1, gama = 2)
        io.imshow(img_gama)
        io.show()
        
        # média e convolução
        psf = np.ones((3, 3)) / 9
        img_conv = conv2(img_gray, psf, 'same')
        io.imshow(img_gray)
        io.show()
    
        #break
