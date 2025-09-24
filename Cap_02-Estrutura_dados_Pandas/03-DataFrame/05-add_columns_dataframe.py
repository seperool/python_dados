#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 14:21:43 2025

@author: sergio
"""

import pandas as pd

#------------------------------------------------------------------------------
# Carregamento e Inspeção Inicial do DataFrame
#------------------------------------------------------------------------------

print("\n--- Carregando o arquivo CSV ---")
df = pd.read_csv("../scientists.csv")

print("\n--- Primeiras 5 linhas do DataFrame ---")
print(df.head(5))

print("\n--- Nomes das colunas ---")
print(df.columns)

print("\n--- Informações do DataFrame ---")
print(df.info())

print("\n--- Dimensões (linhas, colunas) do DataFrame ---")
print(df.shape)

#------------------------------------------------------------------------------
# Conversão de Colunas para o Formato Datetime
#------------------------------------------------------------------------------

print("\n--- Convertendo colunas de data (Born e Died) ---")
born_datetime = pd.to_datetime(df['Born'], format='%Y-%m-%d')
print("\nBorn (coluna convertida para datetime):\n", born_datetime.head())

died_datetime = pd.to_datetime(df['Died'], format='%Y-%m-%d')
print("\nDied (coluna convertida para datetime):\n", died_datetime.head())

#------------------------------------------------------------------------------
# Adicionando Novas Colunas ao DataFrame
#------------------------------------------------------------------------------

print("\n--- Adicionando 'born_dt' e 'died_dt' ao DataFrame ---")
df['born_dt'], df['died_dt'] = (born_datetime, died_datetime)

print("\n--- DataFrame com as novas colunas ---")
print(df.head())

print("\n--- Informações atualizadas do DataFrame (com born_dt e died_dt) ---")
print(df.info())