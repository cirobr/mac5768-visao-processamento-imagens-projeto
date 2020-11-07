import numpy as np
from scipy.signal import convolve2d as conv2
from skimage import io
#from skimage.color import rgb2gray
#from skimage.util import img_as_ubyte
import pandas as pd


# definição de funções de transformação
def transf_grad(img):
    img_aux = np.gradient(img)
    img2 = np.sqrt(np.square(img_aux[0]) + np.square(img_aux[1]))
    return img2

def transf_log2(img, c):
    img2 = c * np.log2(1.0 + img)
    return img2

def transf_gama(img, c, gama):
    img2 = c * np.power(img, gama)
    return img2

# adequação do nome de arquivo nos metadados
def fix_jpeg_name(arq):
    arq2 = int(arq[:-4])
    arq2 = str(arq2) + ".jpg"
    return arq2


# arquivo de metadados em cinza
pasta1 = "./originalGrayDataset/"
metafile1 = "grade-cinza.csv"
filename1 = pasta1 + metafile1
df = pd.read_csv(filename1, sep=";")
print(df.head(5), "\n")

# arquivo de metadados aumentados
pasta2 = "./augmentedDataset/"
metafile2 = "grade-augmented.csv"
filename2 = pasta2 + metafile2

# criar dataframe para metadados aumentados
df2 = pd.DataFrame(data=df, index=df.index, columns=df.columns)

# número do último arquivo
n = df2.tail(1)
n = n["arquivo"]
n = n.values[0]
n = str(n[:-4])
n = int(n)


# transformação de fotos cinza
for ind in df.index:
    #print(df.loc[ind])

    # ler foto cinza
    arq1 = df["arquivo"][ind]
    arq1 = fix_jpeg_name(arq1)
    f1 = pasta1 + arq1
    img_gray = io.imread(f1)
    
    
    ### soma de fundo (gradiente) com foto cinza
    ###
    img_grad = transf_grad(img_gray)
    img_grad = img_gray + img_grad
    img_grad = img_grad.astype(np.uint8)
     
    # nome de arquivo da foto gerada
    n += 1
    arq2 = str(n) + ".jpg"
    f = pasta2 + arq2
    
    # salvar foto gerada
    io.imsave(f, img_grad)
     
    # gravar dados da foto gerada no dataframe
    l = [df.sequencia[ind], df.objeto[ind], df.tipo_obj[ind], df.fundo[ind], df.iluminacao[ind], "grad", df.responsavel[ind], arq2]
    df2.loc[n] = l
    
    ### foto log2
    ###
    img_log2 = transf_log2(img_gray, c = 1)
    #img_log2 = img_log2.astype(np.uint8)
    
    # nome de arquivo da foto gerada
    n += 1
    arq2 = str(n) + ".jpg"
    f = pasta2 + arq2
    
    # salvar foto gerada
    io.imsave(f, img_log2)
     
    # gravar dados da foto gerada no dataframe
    l = [df.sequencia[ind], df.objeto[ind], df.tipo_obj[ind], df.fundo[ind], df.iluminacao[ind], "log", df.responsavel[ind], arq2]
    df2.loc[n] = l
    
    ### foto exponencial
    ###
    img_gama = transf_gama(img_gray, c = 1, gama = 2)

    # nome de arquivo da foto gerada
    n += 1
    arq2 = str(n) + ".jpg"
    f = pasta2 + arq2
    
    # salvar foto gerada
    io.imsave(f, img_gama)
     
    # gravar dados da foto gerada no dataframe
    l = [df.sequencia[ind], df.objeto[ind], df.tipo_obj[ind], df.fundo[ind], df.iluminacao[ind], "exp", df.responsavel[ind], arq2]
    df2.loc[n] = l

    ### média e convolução
    ###
    psf = np.ones((3, 3)) / 9
    img_conv = conv2(img_gray, psf, 'same')
    img_conv = img_conv.astype(np.uint8)

    # nome de arquivo da foto gerada
    n += 1
    arq2 = str(n) + ".jpg"
    f = pasta2 + arq2
    
    # salvar foto gerada
    io.imsave(f, img_conv)
     
    # gravar dados da foto gerada no dataframe
    l = [df.sequencia[ind], df.objeto[ind], df.tipo_obj[ind], df.fundo[ind], df.iluminacao[ind], "conv", df.responsavel[ind], arq2]
    df2.loc[n] = l
    
# salvar metadados aumentados
print(df2.head(5), "\n")
df2.to_csv(filename2, index = False, header=True, sep=";")
