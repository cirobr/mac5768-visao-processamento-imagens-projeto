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

# tamanho da amostra por classe para processamento manual
sample_size = int(len(df1) * 0.15 / 10)

# filtrar metadados
filtro = (df1.fundo == "branco") & (df1.responsavel == "Ciro")
df_temp1 = df1[filtro]
classes = df_temp1["objeto"].unique()

# criar data frame vazio
df2 = pd.DataFrame(data = None, columns = df1.columns)

for classe in classes:
    # selecionar classe
    filtro = (df_temp1.objeto == classe)
    df_temp2 = df_temp1[filtro]
    
    # sortear amostra aleatoria para processamento manual
    seed = 1
    df_temp2 = df_temp2.sample(n            = sample_size,
                               replace      = False, 
                               random_state = seed)
   
    # adicionar df_temp2 a df2
    df2 = df2.append(df_temp2, ignore_index=True)

df2.transformacao = "seg manual"

# copiar fotos para processamento manual
pasta2 = "./manualThresholdDataset/"
metafile2 = "grade.csv"
filename2 = pasta2 + metafile2
df2.to_csv(filename2, 
           index  = False, 
           header = True, 
           sep    = ";")

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
