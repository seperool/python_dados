#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Python para Análise Exploratória de Dados (EDA) e Visualização
usando Pandas, Matplotlib e Seaborn.

Created on Tue Dec 9 13:24:37 2025
@author: sergio

O foco é a criação de um **Pair Plot (Gráfico de Pares)** usando sns.pairplot
para visualizar as relações e distribuições entre todas as variáveis
numéricas do DataFrame.

Função do pairplot (sns.pairplot):
O **sns.pairplot** cria uma grade (matrix) de gráficos onde:
1. **Diagonal principal (kde/hist)**: Exibe a **distribuição** (univariada) de cada variável numérica (por padrão, um Kernel Density Estimate ou Histograma).
2. **Off-diagonal (scatterplot)**: Exibe as **relações de dispersão** (bivariada) entre todos os pares de variáveis. Isso ajuda a identificar correlações e padrões.
"""

# ===============================================
# IMPORTAÇÃO DE BIBLIOTECAS
# ===============================================
import pandas as pd # Alias 'pd' para manipulação e análise de dados (DataFrames)
import numpy as np # Alias 'np' para operações numéricas (mantido, embora não usado no pairplot)
import matplotlib.pyplot as plt # Alias 'plt' para plotagem de gráficos e ajustes de baixo nível
import seaborn as sns # Alias 'sns' para visualização estatística de alto nível

# ===============================================
# CARREGAMENTO DE DADOS
# ===============================================
# Carrega o conjunto de dados 'tips' de exemplo (gorjetas) diretamente do Seaborn
tips = sns.load_dataset("tips")

# ===============================================
# INSPEÇÃO DE DADOS (Análise Exploratória Inicial)
# ===============================================
print("--- Visão Geral do DataFrame (Colunas e Primeiras Linhas) ---") # Imprime um cabeçalho para seção
print(tips.columns) # Exibe o nome de todas as colunas do DataFrame
print(tips.head()) # Exibe as 5 primeiras linhas para inspeção rápida da estrutura
print("-" * 30) # Imprime um separador

print("\n--- Estatísticas Descritivas (describe) ---") # Imprime um cabeçalho para seção
print(tips.describe()) # Gera estatísticas resumidas das colunas numéricas (contagem, média, desvio padrão, quartis)
print("-" * 30) # Imprime um separador

print("\n--- Tipos de Dados e Saúde do DF (info) ---") # Imprime um cabeçalho para seção
# Mostra tipos de dados, contagem de valores não-nulos e uso de memória
tips.info()
print("-" * 30) # Imprime um separador

# ===============================================
# VISUALIZAÇÃO DE DADOS (Pair Plot)
# ===============================================

# Cria o Pair Plot (Gráfico de Pares) usando Seaborn.
# Ele gera uma matriz de gráficos que mostra a relação de dispersão para cada par de colunas numéricas
# e a distribuição de cada coluna na diagonal.
fig = sns.pairplot(tips) # 

# Exibe o gráfico gerado.
plt.show()