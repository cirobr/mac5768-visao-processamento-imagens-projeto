import os
from skimage import io
from skimage.filters import threshold_otsu, threshold_yen
import matplotlib.pyplot as plt

# extrair sufixo do arquivo
def sufixo(arq):
    suf = arq[-4:]
    return suf

# arquivo de entrada em cinza
pasta1 = "./originalGrayDataset"
#pasta1 = "./fotos-teste"
lista_fotos = os.listdir(pasta1)

# arquivos de saída de fotos após threshold
pasta2 = "./thresholdOtsu"
pasta3 = "./thresholdYen"

for foto in lista_fotos:
    if sufixo(foto) != ".jpg":
        continue

    fullname1 = pasta1 + '/' + foto
    print(fullname1)
    img = io.imread(fullname1)
    
    # threshold Otsu
    thresh2 = threshold_otsu(img)
    binary2 = img > thresh2

    # threshold Yen    
    thresh3 = threshold_yen(img)
    binary3 = img > thresh3
    
    # plotagem de fotos "mnist-like"
    plt.close("all")
    f, ax = plt.subplots(1, 3, figsize=(10, 10))

    ax[0].set_title("originalGray")
    ax[0].set(xticks=[], yticks=[])
    ax[0].imshow(img, cmap=plt.cm.gray)

    ax[1].set_title("thresholdOtsu")
    ax[1].set(xticks=[], yticks=[])
    ax[1].imshow(binary2, cmap=plt.cm.gray)
    
    ax[2].set_title("thresholdYen")
    ax[2].set(xticks=[], yticks=[])
    ax[2].imshow(binary3, cmap=plt.cm.gray)
    
    plt.tight_layout()
    io.show()
    
    # gravação das imagens
    f2 = pasta2 + "/" + foto
    io.imsave(f2, binary2)
    
    f3 = pasta3 + "/" + foto
    io.imsave(f3, binary3)
    #break
