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
pasta1 = "./thresholdManual/"
pasta1 = "./fotos-teste/"
metafile1 = "grade.csv"
filename1 = pasta1 + metafile1
df1 = pd.read_csv(filename1, sep=",")
print(df1.head(5), "\n")

# pasta de gravação de fotos bbox
pasta2 = "./bboxManual/"

# identificar classes contidas no arquivo
classes = df1["objeto"].unique()
classes.sort()

#ler imagens por classes
for classe in classes:
    # selecionar registros correspondentes a classe de objeto
    filtro = (df1.objeto == classe)
    df_temp = df1[filtro]
    lista_fotos = df_temp["arquivo"]

    # processar fotos correspondentes a cada classe
    for foto in lista_fotos:
        foto = fix_jpeg_name(foto)
        fullname = pasta1 + foto
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
        f, ax = plt.subplots(1, 2, figsize=(10, 10))
        ax[0].imshow(img2, cmap=plt.cm.gray)
        ax[0].set(xticks=[], yticks=[])
        ax[0].set_title("thresholdManual + Feret Box")

        # gerar e plotar feret boxes
        for r in regions:
            if r.area <= 2000:                  # filtro de pequenos artefatos
                continue
    
            minr, minc, maxr, maxc = r.bbox
            bx = (minc, maxc, maxc, minc, minc)
            by = (minr, minr, maxr, maxr, minr)
            ax[0].plot(bx, by, '-r', linewidth=1.0)
        
        # gerar sub-imagem dentro do feret box
        img2sub = img2[minr:maxr, minc:maxc]
        ax[1].imshow(img2sub, cmap=plt.cm.gray)
        ax[1].set(xticks=[], yticks=[])
        ax[1].set_title("Feret Box")
    
        # mostrar imagens
        plt.tight_layout()
        io.show()
        
        # gravação das imagens
        f2 = pasta2 + foto
        io.imsave(f2, img2sub)

# gravar metadados
metafile2 = metafile1
df2 = df1
df2.transformacao = "bbox manual"
filename2 = pasta2 + metafile2
df2.to_csv(filename2, 
           index = False, 
           header=True, 
           sep=";")
print(df2.head(5), "\n")
