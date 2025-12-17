#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Python para Análise Multivariada e Matrizes de Dispersão
usando Pandas, Matplotlib e Seaborn.

Created on Wed Dec 17 18:11:48 2025
@author: sergio

Este script utiliza a função Pair Plot do Seaborn para visualizar relações
combinadas entre todas as variáveis numéricas do dataset 'tips'. 

O foco é o uso do parâmetro **hue**, que aplica um mapeamento de cores baseado 
na variável categórica 'sex'. Isso permite observar como diferentes grupos 
se comportam em múltiplas correlações simultaneamente, facilitando a 
identificação de clusters e tendências por gênero.
"""

# ===============================================
# IMPORTAÇÃO DE BIBLIOTECAS
# ===============================================
import pandas as pd                 # Alias 'pd' para manipulação e análise de dados (DataFrames)
import numpy as np                  # Alias 'np' para operações numéricas
import matplotlib.pyplot as plt      # Alias 'plt' para ajustes de layout e exibição
import seaborn as sns               # Alias 'sns' para visualização estatística de alto nível

# ===============================================
# CARREGAMENTO DE DADOS
# ===============================================
# Carrega o conjunto de dados 'tips' de exemplo (gorjetas) diretamente do Seaborn
tips = sns.load_dataset("tips")     # Carrega o DataFrame 'tips' (conta total, gorjeta, gênero, etc.)

# ===============================================
# INSPEÇÃO DE DADOS (Análise Exploratória Inicial)
# ===============================================
print("--- Visão Geral do DataFrame (Colunas e Primeiras Linhas) ---") 
print(tips.columns)                 # Exibe o nome de todas as colunas do DataFrame
print(tips.head())                  # Exibe as 5 primeiras linhas para inspeção rápida da estrutura
print("-" * 30)

print("\n--- Estatísticas Descritivas (describe) ---") 
print(tips.describe())              # Gera estatísticas resumidas das colunas numéricas
print("-" * 30)

print("\n--- Tipos de Dados e Saúde do DF (info) ---") 
tips.info()                         # Mostra tipos de dados, contagem de valores não-nulos e memória
print("-" * 30)

# ===============================================
# VISUALIZAÇÃO DE DADOS (Pair Plot com Hue)
# ===============================================
# O pairplot cria uma matriz de gráficos de dispersão para variáveis numéricas
# e histogramas/KDEs na diagonal principal.
fig = sns.pairplot(
    tips,                           # Define o DataFrame de origem
    hue='sex'                       # Segmenta as cores dos pontos e das curvas pela variável de gênero
)

# Adiciona um título à figura completa (acima dos subplots)
fig.fig.suptitle("Matriz de Relacionamentos - Segmentação por Sexo (Hue)", y=1.02)

# ===============================================
# EXIBIÇÃO
# ===============================================
# Renderiza a matriz de gráficos gerada
plt.show()