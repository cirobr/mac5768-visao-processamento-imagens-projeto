import os
from skimage import io
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops
from skimage.morphology import binary_erosion, binary_dilation, opening, closing, white_tophat
from skimage.segmentation import clear_border


"""
import matplotlib.patches as mpatches
from skimage import data
from skimage.morphology import closing, square
"""

# carrega imagens
pasta = "./fotos-teste/"
lista_fotos = os.listdir(pasta)

for foto in lista_fotos:
    fullname = pasta + foto
    img = io.imread(fullname)

    # processamento/melhoria da segmentação
    img_dilat   = binary_dilation(img)
    img_erosion = binary_erosion(img_dilat)
    
    # imagem final para rótulo
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
        if r.area <= 2000:                 # filtro de pequenos artefatos
            continue

        minr, minc, maxr, maxc = r.bbox
        bx = (minc, maxc, maxc, minc, minc)
        by = (minr, minr, maxr, maxr, minr)
        ax.plot(bx, by, '-r', linewidth=1.0)

    plt.tight_layout()
    io.show()
    #break
