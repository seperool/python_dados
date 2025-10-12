#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 12 15:54:25 2025

@author: sergio
"""

# ====================================
# Importação de Bibliotecas
# ====================================
import pandas as pd     # Principal biblioteca para manipulação e análise de dados (DataFrames)

# ====================================
# Leitura de Arquivo
# ====================================
# Lê o arquivo CSV "scientists.csv" e armazena os dados em um DataFrame (df)
df = pd.read_csv("scientists.csv")

# ====================================
# Análise do Arquivo
# ====================================
# Imprime um cabeçalho
print("\n--- Nomes das colunas ---")
# Mostra/Imprime os nomes de todas as colunas presentes no DataFrame
print(df.columns)

# ====================================
# Salvar DataFrame Completo em feather
# ====================================
df.to_feather("scientists.feather")