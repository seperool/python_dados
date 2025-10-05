#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 27 13:27:15 2025

@author: sergio
"""

# --- 1. Importação de Bibliotecas ---

import pandas as pd

# --- 2. Carregamento e Inspeção do DataFrame ---

# --- Carregando e Inspecionando o DataFrame ---
print("\n--- Carregando o arquivo CSV ---")
# Lê o arquivo 'scientists.csv' e cria um DataFrame
df = pd.read_csv("scientists.csv")

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

# --- 3. Exportando dados pickle ---

# Comentário sobre o tipo de arquivo pickle:
#
# O arquivo '.pickle' é um formato de serialização binária nativa do Python.
# Principais pontos:
# - Serialização: Transforma objetos Python (como DataFrames, listas, dicionários) em um fluxo de bytes.
# - Eficiência: É o formato mais eficiente para salvar e carregar objetos Pandas, pois preserva o *tipo* e a *estrutura* exata do DataFrame, sem perdas.
# - Velocidade: O carregamento de dados a partir de um arquivo pickle é geralmente *muito mais rápido* que carregar a partir de CSV ou Excel, pois não há necessidade de *parsing* (interpretação de texto).
# - Uso: Ideal para salvar o estado intermediário de um DataFrame para uso posterior no mesmo ambiente Python.

# Passa uma string como o path para salvar 
# Exemplo path: '../output/scientists_df.pickle'
df.to_pickle('scientists.pickle')

# As três extensões: 
#.p
#.pkl
#.pickle 
# São comumente usadas para salvar arquivos do tipo pickle em Python.