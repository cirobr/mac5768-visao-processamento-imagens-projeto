#import numpy as np
#from scipy.signal import convolve2d as conv2
from skimage import io
from skimage.color import rgb2gray
from skimage.util import img_as_ubyte
import pandas as pd

# arquivo de metadados em cores
pasta1 = "./fotos-teste/"
metafile1 = "grade-fotos.csv"
filename1 = pasta1 + metafile1
df = pd.read_csv(filename1, sep=";")
print(df.head(5), "\n")

# arquivo de metadados em cinza
pasta2 = "./fotos-teste/"
metafile2 = "grade-cinza.csv"
filename2 = pasta2 + metafile2

# adequação do nome de arquivo nos metadados
def fix_jpeg_name(arq):
    arq2 = int(arq[:-4])
    arq2 = str(arq2) + ".jpg"
    return arq2
    

# quantidade de fotos
n = len(df.arquivo)

# criar dataframe vazio para metadados em cinza
df2 = pd.DataFrame(data=None, columns=df.columns)
df2.insert(loc=5, column="transformacao", value=[])
df2_length = len(df2)

# transformação de fotos cinza
for ind in df.index:
    print(df.loc[ind])

    # ler foto colorida para a lista
    print(df.loc[ind])
    arq1 = df["arquivo"][ind]
    arq1 = fix_jpeg_name(arq1)
    f1 = pasta1 + arq1
    img = io.imread(f1)
    
    # gerar foto cinza
    img_gray = rgb2gray(img)
    img_gray = img_as_ubyte(img_gray)   # voltar para níveis 0-255
     
    # nome do arquivo da foto cinza
    arq1 = int(arq1[:-4])
    arq2 = arq1 + n
    arq2 = str(arq2) + ".jpg"
    f = pasta2 + arq2
    
    # salvar foto cinza
    io.imsave(f, img_gray)
     
    # gravar dados da foto cinza no dataframe
    l = [df.sequencia[ind], df.objeto[ind], df.tipo_obj[ind], df.fundo[ind], df.iluminacao[ind], "cinza", df.responsavel[ind], arq2]
    df2.loc[df2_length] = l
    df2_length += 1

# salvar metadados em cinza
print(df2.head(5), "\n")
df2.to_csv(filename2, index = False, header=True, sep=";")
