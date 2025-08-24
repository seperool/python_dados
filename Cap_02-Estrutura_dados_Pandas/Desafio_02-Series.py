#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 24 17:20:58 2025

@author: sergio
"""

import pandas as pd
import numpy as np

# Series

## O que acontecerá se você passar um `index` com os contêineres?

index_dados = ['a','b','c']
index_dict = ['c','a','d','b']

dados_lista = [100,200,300]
dados_tupla = (100,200,300)
dados_ndarray = np.array([100,200,300])
dict_dados = {'a':100,'b': 200, 'c':300}


print("#----------------list----------------#")
s = pd.Series(dados_lista,index=index_dados)
print(s)

print("#----------------tuple----------------#")
s = pd.Series(dados_tupla,index=index_dados)
print(s)

print("#----------------ndarray----------------#")
s = pd.Series(dados_ndarray,index=index_dados)
print(s)

print("#----------------dict----------------#")
s = pd.Series(dict_dados,index=index_dict)
print(s)
