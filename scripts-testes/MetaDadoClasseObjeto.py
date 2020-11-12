'''===============================================================
Disciplina: MAC5768 
Data......: 26/10/2020 
Aluno.....: Josilton / Ciro 
Objetivo..: Ler o metadados das imagens, fazer uma divisão por 
            classe de imagens.
================================================================'''

import pandas as pd

#Estrutura da pasta no GuitHub
pasta = 'originalDataset'
f = 'Meda_Dados.csv'
#f = 'grade-fotos.csv'
fullname = pasta+'/'+f

# Ler arquivo Metadado 
arq = pd.read_csv(fullname, encoding = 'UTF-8',sep=';' )

# Gera um DataFrame apartir do arquivo de Metadado
im = pd.DataFrame(arq)

# Cria lista de classes
garfo =[]
faca =[]
colher =[]
copo =[]
caneca =[]
alicate=[]
chave=[]
caneta =[]
livro =[]
caderno =[]

# Cria um separação das classes apartir do metadado.
for i in im:
   garfo = im.loc[im["objeto"]=='garfo']
   faca = im.loc[im["objeto"]=='faca'] 
   colher = im.loc[im["objeto"]=='colher'] 
   caneca = im.loc[im["objeto"]=='caneca'] 
   alicate = im.loc[im["objeto"]=='alicate'] 
   chave = im.loc[im["objeto"]=='chave'] 
   caneta = im.loc[im["objeto"]=='caneta'] 
   livro = im.loc[im["objeto"]=='livro'] 
   caderno = im.loc[im["objeto"]=='caderno'] 
   
