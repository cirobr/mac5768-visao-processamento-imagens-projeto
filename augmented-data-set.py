# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 00:43:17 2020

@author: ciror
"""

import os
from skimage import io
from skimage.color import rgb2gray
import numpy as np

# definição de funções de transformação
def transf_log2(img, c):
    img2 = c * np.log2(1 + img)
    return img2

def transf_gama(img, c, gama):
    img2 = c * np.power(img, gama)
    return img2


#Informar o caminho da pasta que estão as fotos.
pasta = 'fotos-teste'
lista_fotos = os.listdir(pasta)

# ler fotos e transformar
imagem = []
for foto in lista_fotos:
    # ler a foto
    fullname = pasta + '/' + foto
    imagem.append(io.imread(fullname))

    # foto original
    img = imagem[-1]
    io.imshow(img)
    io.show()

    # foto cinza
    img_gray = rgb2gray(img)
    io.imshow(img_gray)
    io.show()

    # foto log2
    img_log2 = transf_log2(img_gray, c = 1)
    io.imshow(img_log2)
    io.show()

    # foto exponencial
    img_gama = transf_gama(img_gray, c = 1, gama = 2)
    io.imshow(img_gama)
    io.show()
    
    break
