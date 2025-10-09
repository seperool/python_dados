#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 20:39:59 2025

@author: sergio
"""

import pandas as pd


# Caminho do seu arquivo
caminho_do_arquivo = 'scientists.xlsx'

# Abrindo o arquivo XLSX como um DataFrame
# Por padrão, ele lê a primeira aba (sheet)
df = pd.read_excel(caminho_do_arquivo)

# Para verificar as primeiras linhas do DataFrame
print(df.head())