# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23:12:50:35 2020

@author: josilton.sousa
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os
from skimage import data
from skimage.segmentation import clear_border
from skimage.measure import label, regionprops
from skimage.morphology import closing, square
from skimage.color import label2rgb
from skimage.morphology import binary_erosion, binary_dilation, opening, closing, white_tophat
from skimage import io

# carrega imagem de moedas
pasta = "./fotos-teste/"
lista_fotos = os.listdir(pasta)

for foto in lista_fotos:
    fullname = pasta + foto
    img = io.imread(fullname)

    # erosao e dilatação da imagem
    img_dilat   = binary_dilation(img)
    img_erosion = binary_erosion(img_dilat)

    # label image regions
    img_label = label(img_erosion)
    img_label_overlay = label2rgb(image    = img_erosion,
                                  label    = img_label,
                                  bg_label = 0)
    
    # plotagem de fotos "mnist-like"
    plt.close("all")
    f, ax = plt.subplots(1, 4, figsize=(10, 10))

    ax[0].set_title("segmented")
    ax[0].set(xticks=[], yticks=[])
    ax[0].imshow(img, cmap=plt.cm.gray)

    ax[1].set_title("img_dilation")
    ax[1].set(xticks=[], yticks=[])
    ax[1].imshow(img_dilat, cmap=plt.cm.gray)

    ax[2].set_title("img_erosion")
    ax[2].set(xticks=[], yticks=[])
    ax[2].imshow(img_erosion, cmap=plt.cm.gray)
    
    ax[3].set_title("img_overlay")
    ax[3].set(xticks=[], yticks=[])
    ax[3].imshow(img_label_overlay, cmap=plt.cm.gray)

    plt.tight_layout()
    plt.show()
    break
