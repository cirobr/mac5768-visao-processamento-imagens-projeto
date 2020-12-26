from skimage import io
import pandas as pd

# adequação do nome de arquivo nos metadados
def fix_jpeg_name(arq):
    arq2 = int(arq[:-4])
    arq2 = str(arq2) + ".jpg"
    return arq2

# ler metadados em cinza
pasta1 = "./originalGrayDataset/"
metafile1 = "grade.csv"
filename1 = pasta1 + metafile1
df1 = pd.read_csv(filename1, sep=";")
print(df1.head(5), "\n")

# tamanho da amostra para processamento manual
sample_size = int(len(df1) * 0.15 / 2)

# filtrar metadados
filtro = (df1.fundo == "branco") & (df1.responsavel == "Ciro")
df2 = df1[filtro]

# sortear amostra aleatoria para processamento manual
seed = 1
df2 = df2.sample(n=sample_size, 
                 replace=False, 
                 random_state=seed)
df2.transformacao = "seg manual"

# copiar fotos para processamento manual
pasta2 = "./manualThresholdDataset/"
metafile2 = "grade.csv"
filename2 = pasta2 + metafile2
df2.to_csv(filename2, 
           index = False, 
           header=True, 
           sep=";")

for ind in df2.index:
    arq1 = df2["arquivo"][ind]
    arq1 = fix_jpeg_name(arq1)
    f1 = pasta1 + arq1
    img = io.imread(f1)

    arq2 = arq1
    f2 = pasta2 + arq2
    io.imsave(f2, img)
    #break
print(df2.head(5), "\n")
