import numpy as np
from skimage import io
import pandas as pd
import matplotlib.pyplot as plt

# adequação do nome de arquivo nos metadados
def fix_jpeg_name(arq):
    arq2 = int(arq[:-4])
    arq2 = str(arq2) + ".jpg"
    return arq2


# ler arquivo de metadados aumentados
p1 = "./augmentedDataset/"
m1 = "grade-augmented.csv"
f1 = p1 + m1
df = pd.read_csv(f1, sep=";")

# pasta de imagens e histogramas médios
p2 = "./averageAugmentedDataset/"
m2 = "grade-avg-augmented.csv"
f2 = p2 + m2

df2=pd.DataFrame(data=None, columns=("tipo_obj", "arquivo"))
#df2_length = len(df2)

# dimensões das fotos
s = [(3096, 4128), (2608, 4640)]

# lista de classes
classes = ["garfo", "faca", "colher", "copo", "caneca", "alicate", "chave", "caneta", "livro", "caderno"]

# varredura de fotos por classes
for i in range(len(classes)):

    # filtrar df para a classe sob análise
    dfx = df[df.objeto == classes[i]]
    print(dfx.head(5), "\n")
    
    # criar matriz de soma de fotos
    I0 = np.zeros(s[0])
    I1 = np.zeros(s[1])

    # calcular foto média
    n = 0
    for arq in dfx.arquivo:
        arq = fix_jpeg_name(arq)
        f = p1 + arq
        img = io.imread(f)
        n += 1

        if img.shape not in s:
            img = np.transpose(img)

        if img.shape == s[0]:
            I0 = I0 + img
        else:
            I1 = I1 + img

    if np.all(np.equal(I1, 0)):
        Im = np.divide(I0, n)
    else:
        Im = np.divide(I1, n)

    Im = Im.astype(np.uint8)
    
    # nome do arquivo da foto média
    arqx = classes[i] + "-foto-media" + ".jpg"
    fx = p2 + arqx
    
    # salvar foto média
    io.imsave(fx, Im)
    
    # apresentar Im
    io.imshow(Im)
    io.show()
    
    # apresentar histograma
    plt.hist(Im.ravel(), np.linspace(0, 255, 256))
    plt.show()

    # gravar dados da foto média no dataframe
    l = [classes[i], arqx]
    df2.loc[i] = l
    
    # roda o loop apenas uma vez
    #break

# salvar metadados de fotos médias
print(df2, "\n")
df2.to_csv(f2, index = False, header=True, sep=";")
