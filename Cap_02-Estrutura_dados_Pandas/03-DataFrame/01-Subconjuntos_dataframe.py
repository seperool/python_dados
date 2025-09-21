#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 21 18:28:17 2025

@author: sergio
"""

# Importando biblioteca Pandas
import pandas as pd

# Carrega o arquivo CSV em um DataFrame
df = pd.read_csv("../scientists.csv")

# Exibe as 5 primeiras linhas do DataFrame
print(df.head(5))
# Exibe os nomes de todas as colunas
print(df.columns)
# Mostra um resumo do DataFrame (tipos de dados, contagem de valores não-nulos)
print(df.info())
# Exibe as dimensões do DataFrame (linhas, colunas)
print(df.shape)

# Subconjuntos

# --- Seleção de Colunas ---
print("\n-------------Unica Coluna-------------")
# Seleciona uma única coluna pelo nome
age = df["Age"]
print(age)

print("\n-------------Colunas-------------")
# Seleciona múltiplas colunas usando uma lista de nomes
age_and_occupation = df[["Age",'Occupation']]
print(age_and_occupation)

# --- Seleção de Linhas ---

# --- Por Rótulo (loc) ---
print("\n-------------linha pelo rótulo-------------")
# Seleciona uma linha pelo seu rótulo/índice (neste caso, o número 0)
linha_nome_0 = df.loc[0]
print(linha_nome_0)
  
print("\n-------------linhas pelos rótulos-------------")
# Seleciona múltiplas linhas por seus rótulos
linha_nome_0e1 = df.loc[[0,1]]
print(linha_nome_0e1)

# --- Por Posição (iloc) ---
print("\n-------------número da linha iloc-------------")
# Seleciona uma linha pela sua posição numérica (iloc = índice por localização)
linha_0 = df.iloc[0]
print(linha_0)

print("\n-------------números das linhas iloc-------------")
# Seleciona múltiplas linhas pelas suas posições numéricas
linha_1e2e3 = df.iloc[[1,2,3]]
print(linha_1e2e3)

# --- Por Fatiamento (Slicing) ---
print("\n-------------Fatiamento-------------")
# Seleciona linhas usando a notação [start:stop:step]
print(df[0:6:2])