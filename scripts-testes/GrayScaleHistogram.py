'''===============================================================
Disciplina: MAC5768 
Data......: 08/10/2020 
Aluno.....: Josilton / Ciro 
Objetivo..: Ler um conjunto de arquivos com imagens, transformar
            GrayScale e apresentar um histograma das imagens.
================================================================'''
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage.color import rgb2gray

#Informar o caminho da pasta que estão as fotos.
pasta = 'fotos-teste'
arq = os.listdir(pasta)

for i in arq:
    a = pasta + '/' + i
    
    #ler o arquivo
    original = mpimg.imread(a)
    grayscale = rgb2gray(original)
    
    # mostrar a imagem
    #imgplot = plt.imshow(original)
    fig, axes = plt.subplots(1,2, figsize=(8, 4),sharex=True, sharey=True)
    ax = axes.ravel()
    ax[0].imshow(original) # plota a imagem original
    ax[0].set_title("Imagem Original: "+i)
    ax[1].imshow(grayscale, cmap=plt.cm.gray) # plota a imagem em ton de cinza
    ax[1].set_title("Imagem Grayscale: "+i)
    fig.tight_layout()
    plt.show()
    
    # Gera o histograma
    plt.hist(grayscale.ravel(), bins=256, range=(0.0,1.0), fc='k', ec='k')
    
    # Mostra o histograma
    fig.tight_layout()
    plt.title("Histograma da Imagem: "+i)
    plt.show()

#Fim