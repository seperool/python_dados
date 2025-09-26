#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 26 14:03:07 2025

@author: sergio
"""

# --- 1. Importação de Bibliotecas ---

import pandas as pd

# --- 2. Carregamento e Inspeção do DataFrame ---

# --- Carregando e Inspecionando o DataFrame ---
print("\n--- Carregando o arquivo CSV ---")
# Lê o arquivo 'scientists.csv' e cria um DataFrame
df = pd.read_csv("../scientists.csv")

print("\n--- Primeiras 5 linhas do DataFrame ---")
# Exibe as primeiras 5 linhas para uma visualização inicial dos dados
print(df.head(5))

print("\n--- Nomes das colunas ---")
# Mostra os nomes de todas as colunas do DataFrame
print(df.columns)

print("\n--- Informações do DataFrame ---")
# Fornece um resumo conciso do DataFrame, incluindo o tipo de dados e contagem de valores não nulos por coluna
print(df.info())

print("\n--- Dimensões (linhas, colunas) do DataFrame ---")
# Exibe o número de linhas e colunas do DataFrame
print(df.shape)

# --- 3. Descartando Coluna ---

# Descartando a coluna 'Age' do DataFrame 'df'.
# O 'axis=1' é crucial para dizer ao Pandas que você quer remover uma COLUNA, e não uma LINHA.
# O resultado é armazenado em um NOVO DataFrame, 'df_dropped'.

df_dropped = df.drop(['Age'], axis=1)

print("\n--- Nomes das Colunas do Novo DataFrame (sem 'Age') ---")
print(df_dropped.columns)

print("\n--- Dimensões (linhas, colunas) do Novo DataFrame ---")
# Você deve ver o mesmo número de linhas, mas uma coluna a menos.
print(df_dropped.shape)