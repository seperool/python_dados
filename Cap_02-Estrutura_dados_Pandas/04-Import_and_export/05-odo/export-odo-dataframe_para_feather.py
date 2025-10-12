#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 12 16:14:13 2025

@author: sergio
"""

# ====================================
# Importação de Bibliotecas
# ====================================
import pandas as pd      # Principal biblioteca para manipulação e análise de dados (DataFrames)
from odo import odo      # Importa a função odo para movimentação e conversão de dados

# ====================================
# Definição do Caminho
# ====================================
# Define a variável com o caminho/nome do arquivo CSV a ser lido
caminho_do_arquivo = 'scientists.csv'

# ====================================
# Leitura de Arquivo com ODO
# ====================================
# Lê o arquivo CSV usando 'odo' e converte o resultado diretamente para um DataFrame (df)
df = odo(caminho_do_arquivo, pd.DataFrame)

# ====================================
# Análise do Arquivo
# ====================================
# Imprime um cabeçalho
print("\n--- Nomes das colunas ---")
# Mostra/Imprime os nomes de todas as colunas presentes no DataFrame
print(df.columns)

# ====================================
# Exportação do DataFrame para Feather
# ====================================
# Exporta o DataFrame (df) para o formato Feather, infere-se pelo nome do arquivo
odo(df, 'scientists.feather')