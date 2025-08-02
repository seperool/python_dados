#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 30 13:15:12 2025

@author: sergio
"""

# --- SCRIPT: OBTENDO SUBCONJUNTOS DE DADOS EM DATAFRAMES PANDAS ---

import pandas as pd # Importa a biblioteca pandas, atribuindo-lhe o alias 'pd'.

#------------------------------------------------------------------------------

# --- Carregamento e Inspeção Inicial ---

# Carrega o arquivo 'gapminder.tsv' em um DataFrame, usando tabulação como separador.
# df = pd.read_csv('../Data/Cap_01/gapminder.tsv', sep='\t')
df = pd.read_csv(r'C:\Users\Sergio\github\python_dados\Data\Cap_01\gapminder.tsv', sep='\t')

print("--- Informações Completas do DataFrame (df.info()) ---")
print(df.info()) # Exibe um resumo conciso do DataFrame, incluindo tipos de dados e valores não nulos.
print("\n--- Primeiras 5 linhas do DataFrame (df.head()) ---")
print(df.head()) # Mostra as 5 primeiras linhas do DataFrame para uma visualização rápida.

#------------------------------------------------------------------------------

# --- Subconjunto de Colunas ---

print("\n--- Selecionando Colunas ---")

# Seleciona a coluna 'country' do DataFrame 'df' e a armazena em 'country_df'.
country_df = df["country"]
print("\n--- Exibindo a Series 'country' (country_df.head() ---")
print(country_df.head()) # Exibe as 5 primeiras entradas da Series 'country_df'.
print("\n--- Exibindo a Series 'country' (country_df.tail()) ---")
print(country_df.tail()) # Exibe as 5 últimas entradas da Series 'country_df'.

# Seleciona as colunas 'country', 'continent' e 'year' e cria um novo DataFrame 'subset'.
subset = df[['country','continent','year']]
print("\n--- Exibindo as últimas 5 linhas do DataFrame 'subset' (subset.tail()) ---")
print(subset.tail()) # Mostra as 5 últimas linhas do DataFrame 'subset'.

#------------------------------------------------------------------------------

# --- Subconjunto de Linhas ---

print("\n--- Selecionando Linhas com `loc` e `iloc` ---")

# Exibe as primeiras 5 linhas do DataFrame para referência.
print("\nDataFrame original:")
print(df.head()) 

# Seleciona a linha com o rótulo de índice `0` usando `loc`.
print("\nPrimeira linha com df.loc[0]:")
print(df.loc[0]) 

# Seleciona a linha com o rótulo de índice `99`.
print("\nCentésima linha com df.loc[99]:")
print(df.loc[99]) 

# Obtém o número total de linhas do DataFrame.
number_of_rows = df.shape[0] 
# Calcula o índice da última linha (número de linhas - 1).
last_row_index = number_of_rows - 1 
# Seleciona a última linha usando o índice calculado.
print(f"\nÚltima linha com df.loc[{last_row_index}]:")
print(df.loc[last_row_index]) 

# Uma forma mais simples e direta de selecionar a última linha.
print("\nÚltima linha com df.tail(n=1):")
print(df.tail(n=1)) 

# Seleciona as linhas nas posições de índice `0`, `99` e `999` usando `iloc`.
# O `iloc` utiliza posições inteiras, como em listas.
print("\nLinhas nas posições 0, 99 e 999 com df.iloc[[0,99,999]]:")
print(df.iloc[[0, 99, 999]])

#------------------------------------------------------------------------------

# --- Combinando Tudo ---