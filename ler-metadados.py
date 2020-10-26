# -*- coding: utf-8 -*-
'''===============================================================
Disciplina: MAC5768 
Data......: 25/10/2020 
Aluno.....: Ciro 
Objetivo..: Ler o metado das imagens, realizar agrupamento por 
            classe de imagens.
================================================================'''

import pandas as pd
import csv

pasta = 'fotos-teste'
f = 'grade-fotos.csv'
fullname = pasta + '/' + f

with open(fullname, newline = '') as csvfile:
    arq = csv.reader(csvfile, delimiter = ';')
    d = []
    for row in arq:
        d.append(row)
    d[0][0] = 'sequencia'
    df = pd.DataFrame(d) # passa a lista para um Data Frame

print(df)



# Construir agpupamentos dos objetos
#Cp = df.query('2 =="copo"').head()
#print("Imprimit: ",Cp)

#df.query('responsavel in ["Josilton","caneca"]', inplace=True)
#df.head()