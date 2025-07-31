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
df = pd.read_csv('../Data/Cap_01/gapminder.tsv', sep='\t')

print("--- Informações Completas do DataFrame (df.info()) ---")
print(df.info()) # Exibe um resumo conciso do DataFrame, incluindo tipos de dados e valores não nulos.
print("--- Primeiras 5 linhas do DataFrame (df.head()) ---")
print(df.head()) # Mostra as 5 primeiras linhas do DataFrame para uma visualização rápida.

#------------------------------------------------------------------------------

# --- Subconjunto de Colunas ---

# Seleciona a coluna 'country' do DataFrame 'df' e a armazena em 'country_df'.
country_df = df["country"]
print(country_df.head()) # Exibe as 5 primeiras entradas da Series 'country_df'.
print(country_df.tail()) # Exibe as 5 últimas entradas da Series 'country_df'.

# Seleciona as colunas 'country', 'continent' e 'year' e cria um novo DataFrame 'subset'.
subset = df[['country','continent','year']]
print(subset.tail()) # Mostra as 5 últimas linhas do DataFrame 'subset'.

#------------------------------------------------------------------------------

# --- Subconjunto de Linhas ---
# --- Combinando Tudo ---