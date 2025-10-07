#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 17:27:09 2025

@author: sergio
"""

# ====================================
# Importação de Bibliotecas
# ====================================
import pandas as pd     # Principal biblioteca para manipulação e análise de dados (DataFrames)
import xlwt             # Biblioteca para escrever arquivos Excel antigos (.xls)
import openpyxl         # Biblioteca para ler/escrever arquivos Excel modernos (.xlsx)

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
# Salvar DataFrame Completo em Excel
# ====================================
# Salva o DataFrame completo em um novo arquivo Excel (.xlsx)
df.to_excel('scientists.xlsx',
             # Define o nome da aba (planilha)
             sheet_name='scientists',
             # Não inclui o índice do DataFrame como uma coluna
             index=False)

# ====================================
# Converter Series em DataFrame
# ====================================
# Seleciona apenas a coluna 'Name' do DataFrame original (df)
name_scientists = df['Name']
# Converte a Series (coluna) 'name_scientists' de volta para um DataFrame ('names_df')
names_df = name_scientists.to_frame()

# ====================================
# Salvar Novo DataFrame (Apenas Nomes)
# ====================================
# Salva o novo DataFrame contendo apenas os nomes em outro arquivo Excel (.xlsx)
names_df.to_excel('scientists_names.xlsx')