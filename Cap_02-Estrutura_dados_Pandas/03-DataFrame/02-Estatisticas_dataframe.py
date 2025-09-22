#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 21 19:59:13 2025

@author: sergio
"""

import pandas as pd

# Carrega o arquivo CSV para um DataFrame
df = pd.read_csv("../scientists.csv")

# Exibe as 5 primeiras linhas do DataFrame
print("5 Primeiras linhas do DataFrame:")
print(df.head(5))

# Exibe os nomes das colunas
print("\nColunas do DataFrame:")
print(df.columns)

# Fornece um resumo conciso do DataFrame, incluindo o tipo de dado de cada coluna e a memória utilizada
print("\nPrincipais informações do DataFrame:")
print(df.info())

# Retorna uma tupla representando as dimensões do DataFrame (linhas, colunas)
print("\nDimensão do DataFrame:")
print(df.shape)

#------------------------------------------------------------------------------
print("\n-------------------------------------------------------\n")
# Funções de estatística

# min(): Retorna o valor mínimo de uma coluna
# Vamos supor que a coluna de idade se chame 'Age'
print("Idade mínima:", df['Age'].min())

# max(): Retorna o valor máximo de uma coluna
print("Idade máxima:", df['Age'].max())

# mean(): Retorna a média dos valores de uma coluna
print("Idade média:", df['Age'].mean())

# median(): Retorna a mediana dos valores de uma coluna
print("Mediana da idade:", df['Age'].median())

# mode(): Retorna a moda (valor mais frequente) de uma coluna
print("Moda da idade:", df['Age'].mode())

# quantile(): Retorna o valor no quartil especificado. Exemplo: 0.25 para o 1º quartil
print("1º Quartil (25%) da idade:", df['Age'].quantile(0.25))

# replace(): Substitui valores em uma coluna
# Exemplo: Substitui "Male" por "Homem" e "Female" por "Mulher" na coluna 'Gender'
# df['Gender'] = df['Gender'].replace({'Male': 'Homem', 'Female': 'Mulher'})
# print(df.head())

# sample(): Retorna uma amostra aleatória de linhas do DataFrame
# Exemplo: Retorna 3 linhas aleatórias
print("\nAmostra aleatória de 3 linhas:")
print(df.sample(3))

# sort_values(): Ordena o DataFrame com base nos valores de uma coluna
# Exemplo: Ordena o DataFrame pela idade, da menor para a maior
print("\nDataFrame ordenado por idade:")
print(df.sort_values(by='Age'))

# unique(): Retorna os valores únicos de uma coluna
# Exemplo: Retorna os países únicos
print("\nPaíses únicos:")
print(df['Name'].unique())

# Usa a função describe() para obter estatísticas resumidas das colunas numéricas
print("\nResumo estatístico:")
print(df.describe())