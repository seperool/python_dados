#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 12 16:03:59 2025

@author: sergio
"""

# ====================================
# Importação de Bibliotecas
# ====================================
import pandas as pd     # Principal biblioteca para manipulação e análise de dados (DataFrames)
from odo import odo

caminho_do_arquivo = 'scientists.csv'

# ====================================
# Leitura de Arquivo
# ====================================
# Lê o arquivo CSV "scientists.csv" e armazena os dados em um DataFrame (df)
df = odo(caminho_do_arquivo, pd.DataFrame)

# ====================================
# Análise do Arquivo
# ====================================
# Imprime um cabeçalho
print("\n--- Nomes das colunas ---")
# Mostra/Imprime os nomes de todas as colunas presentes no DataFrame
print(df.columns)
