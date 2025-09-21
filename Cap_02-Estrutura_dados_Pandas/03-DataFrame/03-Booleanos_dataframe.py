#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 21 19:37:13 2025

@author: sergio
"""

import pandas as pd

# Carrega o arquivo CSV
df = pd.read_csv("../scientists.csv")

# Exibe as 5 primeiras linhas do DataFrame
print("\n--- Primeiras 5 linhas ---")
print(df.head(5))

# Exibe os nomes das colunas
print("\n--- Nomes das colunas ---")
print(df.columns)

# Mostra informações sobre as colunas e dados
print("\n--- Informações do DataFrame ---")
print(df.info())

# Exibe as dimensões (linhas, colunas)
print("\n--- Dimensões do DataFrame ---")
print(df.shape)

# Filtra por idade maior que a média
bool1 = df[df['Age'] > df['Age'].mean()]
print("\n--- Um booleano ---")
print("\n--- Filtro: idade acima da média ---")
print(bool1)

# Filtra por idade maior que a média E maior ou igual à moda
bool2 = df[(df['Age'] > df['Age'].mean()) &\
           (df['Age'] >= df['Age'].mode()[0])]
print("\n--- Vários booleanos ---")
print("\n--- Filtro: idade acima da média E maior ou igual à moda ---")
# Para combinar múltiplos filtros, use & (E), | (OU) e ~ (NÃO).
print(bool2)