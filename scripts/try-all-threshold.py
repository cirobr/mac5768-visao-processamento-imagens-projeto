import os
from skimage import io
from skimage.filters import try_all_threshold
import matplotlib.pyplot as plt


# arquivo de entrada em cinza
pasta1 = "./originalGrayDataset/"
lista_fotos = os.listdir(pasta1)

i = 0
for foto in lista_fotos:
    fullname1 = pasta1 + foto
    img = io.imread(fullname1)
    fig, ax = try_all_threshold(img, figsize=(10, 8), verbose=False)
    plt.show()

    i += 1
    if i > 10:
        break
