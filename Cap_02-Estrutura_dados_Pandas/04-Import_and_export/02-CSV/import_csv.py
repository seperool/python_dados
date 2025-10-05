#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  3 16:41:39 2025

@author: sergio
"""

# --- 1. Importação de Bibliotecas ---

# Importa a biblioteca pandas, fundamental para manipulação e análise de dados
import pandas as pd

# --- 2. Importação do Arquivo de Dados ---

# Carrega o arquivo 'scientists.csv' em um DataFrame do pandas chamado 'df'
df = pd.read_csv('scientists.csv')

# --- 3. Inspeção do DataFrame ---

# Imprime o cabeçalho descritivo da seção
print("\n--- Primeiras 5 linhas do DataFrame ---")
# Exibe as primeiras 5 linhas para uma visualização inicial dos dados
print(df.head(5))

# Imprime o cabeçalho descritivo da seção
print("\n--- Nomes das colunas ---")
# Mostra os nomes de todas as colunas do DataFrame
print(df.columns)

# Imprime o cabeçalho descritivo da seção
print("\n--- Informações do DataFrame ---")
# Fornece um resumo conciso do DataFrame (tipos de dados, contagem de valores não nulos e uso de memória)
print(df.info())

# Imprime o cabeçalho descritivo da seção
print("\n--- Dimensões (linhas, colunas) do DataFrame ---")
# Exibe o número de linhas e colunas do DataFrame (formato: (linhas, colunas))
print(df.shape)