# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 18:16:37 2020

@author: cirob
"""

filename = "./fotos-teste/grade_fotos.csv"
f = open(filename, "r")
l = f.readline()
print(l)
l = str.split(l, ";")
l[0] = l[0][3:]
print(l)

f.close()