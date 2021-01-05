import os
import pandas as pd
from skimage import io
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops
from skimage.morphology import binary_erosion, binary_dilation

# adequação do nome de arquivo nos metadados
def fix_jpeg_name(arq):
    arq2 = int(arq[:-4])
    arq2 = str(arq2) + ".jpg"
    return arq2

# ler metadados segmentação manual
pasta = "./fotos-teste/"
metafile = "grade.csv"
filename = pasta + metafile
df = pd.read_csv(filename, sep=",")
print(df.head(5), "\n")

# identificar classes contidas no arquivo
classes = df["objeto"].unique()
classes.sort()

#ler imagens por classes
for classe in classes:
    # selecionar registros correspondentes a classe de objeto
    filtro = (df.objeto == classe)
    df_temp = df[filtro]
    lista_fotos = df_temp["arquivo"]

    # processar fotos correspondentes a cada classe
    for foto in lista_fotos:
        foto = fix_jpeg_name(foto)
        fullname = pasta + foto
        img = io.imread(fullname)
    
        # processamento/melhoria da segmentação
        img_dilat   = binary_dilation(img)
        img_erosion = binary_erosion(img_dilat)
        
        # imagem final para label
        img2 = img_erosion
    
        # label image regions
        img_label = label(img2, background=1)   # background=1 (fundo branco)
        regions = regionprops(img_label)
    
        # plotagem de fotos identificadas
        plt.close("all")
        fig, ax = plt.subplots()
        ax.imshow(img2, cmap=plt.cm.gray)
        ax.set(xticks=[], yticks=[])
    
        # gerar feret boxes
        for r in regions:
            if r.area <= 2000:                  # filtro de pequenos artefatos
                continue
    
            minr, minc, maxr, maxc = r.bbox
            bx = (minc, maxc, maxc, minc, minc)
            by = (minr, minr, maxr, maxr, minr)
            ax.plot(bx, by, '-r', linewidth=1.0)
    
        # mostrar imagem
        plt.tight_layout()
        io.show()
        
        # gravação das imagens
        ### @ Josilton, não sei como gravar uma imagem composta pela imagem original e caixas
        ### pediria sua ajuda para verificar. obgd!
    
        #break
