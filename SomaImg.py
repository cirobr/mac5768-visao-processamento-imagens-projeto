'''===============================================================
Disciplina: MAC5768 
Data......: 26/10/2020 
Aluno.....: josilton / Ciro 
Objetivo..: Ler o metadados das imagens, fazer uma divisão por 
            classe de imagens.
            Ler arquivo .jpg comparar com a classe do metadado e
            soma as imagem e a média das imagens.
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

#===================================================
# Ler arquivo Metadado e transforma em um Data Frame
#===================================================
imgtest = pd.read_csv(fullname, encoding = 'UTF-8',sep=';' )
Df_imgtest = pd.DataFrame(imgtest)

#=======================================================
# Cria uma lista para receber os objetos das classes.
#=======================================================
copo=[]
caneca=[]
alicate=[]
chave=[]
#===================================================
# Monta classe de objeto
#===================================================
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


#===================================================
# ler as imagens na pasta do GuitHub
# Informar o caminho da pasta que estão as fotos.
#===================================================
pasta = 'fotos-teste'
os.chdir(pasta)
 
#=======================================================
# Separa os objetos copo comparando com o Metadado
# Gera imagem grayScale
# Alimenta um array com as imagens
#=======================================================
sImg_Copo = []
for e in glob.glob("*.jpg"):
    for a in img_copo:
        if e == a:
            original = mpimg.imread(e)
            grayscale = rgb2gray(original)
            sImg_Copo.append(grayscale)
            print('img_copo :',e)                        # Mostra os arquivos que serão agrupados

#===================================================
# Obtem a soma e a média das imagens copo
#===================================================
Soma_copo = np.sum(sImg_Copo, axis=0)                    # Soma da imagens
Media_copo = np.sum(sImg_Copo, axis=0) / len(sImg_Copo)  # Media das imagens

io.imshow(Soma_copo)
io.show()
io.imshow(Media_copo)
io.show()

       
#=======================================================
# Separa os objetos caneca comparando com o Metadado
# Gera imagem grayScale
# Alimenta um array com as imagens
#=======================================================

sImg_Caneca=[]
for e in glob.glob("*.jpg"):
    for a in img_caneca:
        if e == a:
            original = mpimg.imread(e)
            grayscale = rgb2gray(original)
            sImg_Caneca.append(grayscale)
            print('img_caneca: ',e)

#===================================================
# Obtem a soma e a média das imagens caneca
#===================================================
Soma_caneca = np.sum(sImg_Caneca, axis=0)                      # Soma da imagens
Media_caneca = np.sum(sImg_Caneca, axis=0) / len(sImg_Caneca)  # Media das imagens

io.imshow(Soma_caneca)
io.show()
io.imshow(Media_caneca)
io.show()

#=======================================================
# Separa os objetos alicate comparando com o Metadado
# Gera imagem grayScale
# Alimenta um array com as imagens
#=======================================================          

sImg_alicate =[]
for e in glob.glob("*.jpg"):
    for a in img_alicate:
        if e == a:
            original = mpimg.imread(e)
            grayscale = rgb2gray(original)
            sImg_alicate.append(grayscale)
            print('img_alicate: ',e)

#===================================================
# Obtem a soma e a média das imagens alicate
#===================================================
Soma_alicate = np.sum(sImg_alicate, axis=0)                       # Soma da imagens
Media_alicate = np.sum(sImg_alicate, axis=0) / len(sImg_alicate)  # Media das imagens

io.imshow(Soma_alicate)
io.show()
io.imshow(Media_alicate)
io.show()

#=======================================================
# Separa os objetos chave comparando com o Metadado
# Gera imagem grayScale
# Alimenta um array com as imagens
#=======================================================
sImg_chave=[]
for e in glob.glob("*.jpg"):
    for a in img_chave:
        if e == a:
            original = mpimg.imread(e)
            grayscale = rgb2gray(original)
            sImg_chave.append(grayscale)
            print('img_chave: ',e)

#===================================================
# Obtem a soma e a média das imagens chave
#===================================================
Soma_chave = np.sum(sImg_chave, axis=0)                     # Soma da imagens
Media_chave = np.sum(sImg_chave, axis=0) / len(sImg_chave)  # Media das imagens

io.imshow(Soma_chave)
io.show()
io.imshow(Media_chave)
io.show()