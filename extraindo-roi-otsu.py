import pandas as pd
from skimage import io, img_as_ubyte
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops
from skimage.morphology import binary_erosion, binary_dilation

# adequação do nome de arquivo nos metadados
def fix_jpeg_name(arq):
    arq2 = int(arq[:-4])
    arq2 = str(arq2) + ".jpg"
    return arq2

# ler metadados segmentação manual
pasta1 = "./thresholdOtsu/"
metafile1 = "grade.csv"
filename1 = pasta1 + metafile1
df1 = pd.read_csv(filename1, sep=";")
print(df1.head(5), "\n")

# pasta de gravação de fotos bbox
pasta2 = "./bboxOtsu/"

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

        # identificar região com máxima área e usá-la como feature
        area_region = [r.area for r in regions]
        max_value = max(area_region)
        max_index = area_region.index(max_value)
        r = regions[max_index]
    
        # gerar e plotar feret boxes
        minr, minc, maxr, maxc = r.bbox
        bx = (minc, maxc, maxc, minc, minc)
        by = (minr, minr, maxr, maxr, minr)
        
        # gerar sub-imagem dentro do feret box
        img2sub = img2[minr:maxr, minc:maxc]
        img2sub = img_as_ubyte(img2sub)

        # gravação das imagens
        f2 = pasta2 + foto
        io.imsave(f2, img2sub)

# gravar metadados
metafile2 = metafile1
df2 = df1
df2.transformacao = "bbox otsu"
filename2 = pasta2 + metafile2
df2.to_csv(filename2, 
           index = False, 
           header=True, 
           sep=";")
print(df2.head(5), "\n")
