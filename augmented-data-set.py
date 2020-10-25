# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 00:43:17 2020

@author: ciror
"""

import os
from skimage import io
from skimage.color import rgb2gray
import numpy as np

#Informar o caminho da pasta que estão as fotos.
pasta = 'fotos-teste'
lista_fotos = os.listdir(pasta)

imagem = []
for foto in lista_fotos:
    # ler a foto
    fullname = pasta + '/' + foto
    imagem.append(io.imread(fullname))

    # mostrar a foto original
    img = imagem[-1]
    io.imshow(img)
    io.show()

    # mostrar foto cinza
    img_gray = rgb2gray(img)
    io.imshow(img_gray)
    io.show()

    # mostrar foto log10
    img_log = np.log(img_gray)
    io.imshow(img_log)
    io.show()

    # mostrar foto e (2,718...)
    img_exp = np.exp(img_gray)
    io.imshow(img_exp)
    io.show()