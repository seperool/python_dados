#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 12:14:58 2025

@author: sergio
"""

# --- 1. Importação de Bibliotecas ---

import pandas as pd
import random

# --- 2. Carregamento e Inspeção do DataFrame ---

# --- Carregando e Inspecionando o DataFrame ---
print("\n--- Carregando o arquivo CSV ---")
# Lê o arquivo 'scientists.csv' e cria um DataFrame
df = pd.read_csv("../scientists.csv")

print("\n--- Primeiras 5 linhas do DataFrame ---")
# Exibe as primeiras 5 linhas para uma visualização inicial dos dados
print(df.head(5))

print("\n--- Nomes das colunas ---")
# Mostra os nomes de todas as colunas do DataFrame
print(df.columns)

print("\n--- Informações do DataFrame ---")
# Fornece um resumo conciso do DataFrame, incluindo o tipo de dados e contagem de valores não nulos por coluna
print(df.info())

print("\n--- Dimensões (linhas, colunas) do DataFrame ---")
# Exibe o número de linhas e colunas do DataFrame
print(df.shape)

# --- 3. Manipulação e Embaralhamento de Coluna ---

# A linha a seguir embaralha os valores da coluna 'Age'
# df['Age'] = ... atribui o resultado da operação de volta à coluna 'Age'
# df['Age'].sample(...) seleciona aleatoriamente todos os valores da coluna
# len(df['Age']) garante que todas as idades serão amostradas
# random_state=24 torna o embaralhamento reproduzível (o resultado será o mesmo toda vez que o código rodar)
# .reset_index(drop=True) remove o índice original e cria um novo, garantindo a atribuição correta
df['Age'] = df['Age'].\
    sample(len(df['Age']),random_state=24).\
        reset_index(drop=True)

print("\n--- Alterando (embaralhando) a coluna 'Age' do DataFrame ---")
# Exibe a coluna 'Age' após o embaralhamento para mostrar a mudança
print(df['Age'])

# --- 4. Explicação de Alteração Inplace ---

# A operação acima é considerada uma alteração 'inplace' porque o resultado da
# manipulação da coluna ('sample' e 'reset_index') é atribuído diretamente de
# volta à coluna original (df['Age']). Isso modifica o DataFrame original
# em vez de criar uma nova cópia. Embora o método 'sample' não tenha um
# parâmetro 'inplace', a atribuição 'df['Age'] = ...' efetivamente faz a alteração
# no lugar, economizando memória.
