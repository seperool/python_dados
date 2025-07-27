# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Atributos e Métodos Pandas estudados neste código:
#
# Atributos:
# - .shape: Dimensões (linhas, colunas) do DataFrame.
# - .columns: Nomes das colunas do DataFrame.
# - .dtypes: Tipos de dados de cada coluna.
#
# Métodos:
# - pd.read_csv(): Carrega dados de arquivo em um DataFrame.
# - .head(): Exibe as primeiras N linhas do DataFrame.
# - .info(): Resumo conciso do DataFrame (tipos, não-nulos, memória).

import pandas as pd # Importa a biblioteca pandas como 'pd'.

# --- Carregamento e Inspeção Inicial ---
df = pd.read_csv('../Data/Cap_01/gapminder.tsv', sep='\t')
# Carrega o arquivo TSV em um DataFrame, usando tabulação como separador.

print("--- Primeiras 5 linhas do DataFrame (df.head()) ---")
print(df.head()) # Exibe as 5 primeiras linhas do DataFrame para uma inspeção rápida.

# --- Dimensões do DataFrame ---
print("--- Número de Linhas e Colunas (df.shape) ---")
print(df.shape) # Mostra o número de linhas e colunas (formato: (linhas, colunas)).

# --- Nomes das Colunas ---
print("--- Nomes das Colunas (df.columns) ---")
print(df.columns) # Exibe os nomes de todas as colunas.

# --- Tipos de Dados ---
print("--- Tipos de Dados de Cada Coluna (df.dtypes) ---")
print(df.dtypes) # Mostra o tipo de dado de cada coluna (ex: int64, float64, object).

# --- Informações Gerais do DataFrame ---
print("--- Informações Completas do DataFrame (df.info()) ---")
print(df.info()) # Fornece um resumo completo, incluindo tipos, contagem de não-nulos e uso de memória.