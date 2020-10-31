'''===============================================================
Disciplina: MAC5768 
Data......: 26/10/2020 
Aluno.....: josilton / Ciro 
Objetivo..: Ler o metado das imagens, faz uma divisão por 
            classe de imagens.
            Ler arquivo .jpg compara com a classe do metadado e
            soma as images.
================================================================'''

import glob 
import pandas as pd
import os
from skimage import io
from skimage.color import rgb2gray
import numpy as np
import matplotlib.image as mpimg

#Estrutura da pasta no GuitHub
pasta = 'fotos-teste'
f = 'grade_fotos.csv'
#f = 'grade-fotos.csv'
fullname = pasta+'/'+f

# Ler arquivo Metadado 
imgtest = pd.read_csv(fullname, encoding = 'UTF-8',sep=';' )

Df_imgtest = pd.DataFrame(imgtest)

# Classe Objeto
copo=[]
caneca=[]
alicate=[]
chave=[]

# Monta classe de opbeto
for i in Df_imgtest:
    copo = Df_imgtest.loc[Df_imgtest["objeto"]=='copo']
    img_copo=(copo['arquivo'])
    caneca = Df_imgtest.loc[Df_imgtest["objeto"]=='caneca']
    img_caneca=(caneca['arquivo'])
    alicate = Df_imgtest.loc[Df_imgtest["objeto"]=='alicate']
    img_alicate=(alicate['arquivo'])
    chave = Df_imgtest.loc[Df_imgtest["objeto"]=='chave']
    img_chave=(chave['arquivo'])
#print(Df_imgtest)

# ler as imagens
#Informar o caminho da pasta que estão as fotos.
pasta = 'fotos-teste'
os.chdir(pasta)

# separa as imagens apartir do metadado de classe 
grayscale=[]
for e in glob.glob("*.jpg"):
    for a in img_copo:
        if e == a:
            original = mpimg.imread(e)
            grayscale = rgb2gray(original)
            sImg = np.chararray.sum(grayscale)
            io.imshow(sImg)
            io.show()
            print('img_copo :',e)
       
'''   
for e in glob.glob("*.jpg"):
    for a in img_caneca:
        if e == a:
            original = mpimg.imread(e)
            grayscale = rgb2gray(original)
            print('img_caneca: ',e)
   
            
for e in glob.glob("*.jpg"):
    for a in img_alicate:
        if e == a:
            original = mpimg.imread(e)
            grayscale = rgb2gray(original)
            print('img_alicate: ',e)


for e in glob.glob("*.jpg"):
    for a in img_chave:
        if e == a:
            original = mpimg.imread(e)
            grayscale = rgb2gray(original)
            print('img_chave: ',e)
'''
