#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 12 15:58:15 2025

@author: sergio
"""

# ====================================
# Importação de Bibliotecas
# ====================================
import pandas as pd      # Principal biblioteca para manipulação e análise de dados (DataFrames)

# ====================================
# Definição do Caminho
# ====================================
# Define a variável com o caminho/nome do arquivo Feather a ser lido
caminho_do_arquivo = 'scientists.feather'

# ====================================
# Leitura do Arquivo Feather
# ====================================
# Abre o arquivo Feather e armazena os dados em um DataFrame (df)
df = pd.read_feather(caminho_do_arquivo)

# ====================================
# Verificação Inicial
# ====================================
# Imprime as 5 primeiras linhas do DataFrame para inspeção inicial
print(df.head())