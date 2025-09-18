#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  1 02:15:30 2025

@author: sergio
"""

import pandas as pd # Importa a biblioteca Pandas.

# Carrega um arquivo CSV em um DataFrame do Pandas.
scientists = pd.read_csv("/home/sergio/Programacao/python_dados/Data/Cap_02/scientists.csv")

print("Investigando dados")

print("\n5 Primeiras linhas:")
print(scientists.head(n=5)) # Exibe as 5 primeiras linhas do DataFrame.

print("\nInformações dos dados:")
print(scientists.info()) # Exibe informações sobre o DataFrame (tipos de dados, contagem de valores não-nulos, etc.).

print("Extraindo Series age do dataframe:")
ages = scientists["Age"] # Cria uma Series extraindo a coluna 'Age'.
print(ages.head()) # Exibe as 5 primeiras linhas da Series 'ages'.

print("Estatística básica relacionada aos dados:")
print(ages.describe()) # Exibe estatísticas descritivas da Series 'ages' (média, desvio padrão, quartis, etc.).

print("\n----------Métodos------------")

print("\nMínimo:")
print(ages.min()) # Calcula e exibe o valor mínimo.

print("\nMáximo:")
print(ages.max()) # Calcula e exibe o valor máximo.

print("\nMédia:")
print(ages.mean()) # Calcula e exibe a média aritmética.

print("\nMediana:")
print(ages.median()) # Calcula e exibe a mediana.

print("\nModa:")
print(ages.mode()) # Calcula e exibe a moda.

print("\nDesvio-padrão:")
print(ages.std()) # Calcula e exibe o desvio padrão.

print("\n----------Booleanos------------")

# Filtra a Series, exibindo apenas os valores que são maiores que a média.
print(f"\nAchar as idades maiores que a média {ages.mean()}:")
print(ages[ages > ages.mean()])

print("\nObtém os índices 0, 1, 4, 5 e 7")
# Cria uma lista de booleanos para filtrar a Series.
manual_bool_values = [True,True,False,False,True,True,False,True]
print(ages[manual_bool_values]) # Filtra a Series usando a lista de booleanos, retornando apenas os valores correspondentes a 'True'.