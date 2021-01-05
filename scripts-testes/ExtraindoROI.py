# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23:12:50:35 2020

@author: josilton.sousa
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os
from skimage import data
from skimage.filters import threshold_otsu, threshold_isodata, threshold_li, threshold_mean, threshold_minimum, threshold_triangle, threshold_yen
from skimage.segmentation import clear_border
from skimage.measure import label, regionprops
from skimage.morphology import closing, square
from skimage.color import label2rgb
from skimage.morphology import erosion, dilation, opening, closing, white_tophat
from skimage.morphology import disk
from skimage import io

# carrega imagem de moedas
f = "./fotos-teste/"
lista_fotos = os.listdir(f)

for a in lista_fotos:
    fot = f+a
    image = io.imread(fot)

    # Aplicando threshold
    # Binarina a imagem para separar o ROI (Região de intere) do Fundo
    #thresh = threshold_otsu(image)
    #thresh = threshold_isodata(image)
    #thresh = threshold_li(image)
    #thresh = threshold_mean(image)
    #thresh = threshold_minimum(image)  # melhor resultado de limiaridade para algumas umagens
    #thresh = threshold_triangle(image)
    #thresh = threshold_yen(image)
    thresh = 10
    bw = opening(image < thresh, square(1))
    
    #Processo morfilogico dilatacao da imagem    
    selem=disk(4)  
    img_dilat = dilation(bw,selem)
    
    # É necessário aplicar filtros de morfologia ( erosao e dilatacao) para melhorar a imagem
    
    # remove artifacts connected to image border
    cleared = clear_border(img_dilat)
    
    # label image regions
    label_image = label(cleared)
    image_label_overlay = label2rgb(label_image, image=bw, bg_label=0)
    
    
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.imshow(image_label_overlay)
    
    for region in regionprops(label_image):
        # take regions with large enough areas
        if region.area >= 100:
            # draw rectangle around segmented coins
            minr, minc, maxr, maxc = region.bbox
            rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                                      fill=False, edgecolor='red', linewidth=4)
                                 
            ax.add_patch(rect)
    
    #io.imsave(s, rect)    
    ax.set_axis_off()
    plt.tight_layout()
    plt.show()
