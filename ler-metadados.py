# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 16:16:42 2020
@author: ciror
"""
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

print(d)