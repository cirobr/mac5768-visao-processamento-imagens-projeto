import os
import numpy as np
from skimage import io
from skimage import exposure
from skimage.util import img_as_ubyte
import pandas as pd
import matplotlib.pyplot as plt


# arquivo de entrada em cinza
pasta1 = 'C:/Imagem/averageGrayPicture'
metafile1 = 'grade-avg-gray-pic.csv'
filename1 = pasta1 + "/" + metafile1

df = pd.read_csv(filename1, sep=";")

lista_fotos = os.listdir(pasta1)

# arquivo de saída normalizada
#pasta2 = "C:/Imagem/averageGrayPicture"
#etafile2 = "grade-augmented-normalized.csv"
#filename2 = pasta2 + "/" + metafile2

classes=('alicate',"garfo", "faca", "colher", "copo",'caneca','chave','caneta','livro','caderno')

# varredura de fotos por classes
for i in range(len(classes)):
    # filtrar df para a classe sob análise
    df2 = df[df.tipo_obj == classes[i]]
    print(df2.head(5), "\n")
    
    
    # normalização de fotos
    for foto in lista_fotos:  
        fullname1 = pasta1 + '/' + foto
        img = io.imread(fullname1)
        # normatização do histograma
        img_norm = exposure.equalize_hist(img, nbins = 256)
        img_norm2 = img_as_ubyte(img_norm)
        # normatização adaptativa do histograma
        img_adapteq = exposure.equalize_adapthist(img, clip_limit=0.03)
        print('Imprimindo Classe', foto)
         # apresentar Im
        io.imshow(img)
        io.show()
        plt.hist(img.ravel(), np.linspace(0, 255, 256))
        plt.title("Imagem histograma soma de imagens")
        plt.show()
        io.imshow(img_norm2)
        io.show()
        plt.title("Imagem histograma equalizado")
        plt.hist(img_norm2.ravel(), np.linspace(0, 255, 256))
        plt.show()
        io.imshow(img_adapteq)
        io.show()
        plt.hist(img_adapteq.ravel(), bins=256, range=(0.0,1.0))
        plt.title("Imagem histograma adaptativo")
        plt.show()
        
        #break


