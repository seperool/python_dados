#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Python para Análise de Correlação e Mapeamento de Cores (Hue)
usando Pandas, Matplotlib e Seaborn.

Created on Wed Dec 17 18:08:47 2025
@author: sergio

Este script utiliza o conjunto de dados 'tips' para explorar a relação entre 
o valor da conta e a gorjeta. O foco é a aplicação do parâmetro **hue**, 
que permite segmentar os dados visualmente por cores com base em uma 
variável categórica (neste caso, 'sex').

O uso do 'hue' no Seaborn facilita a identificação de padrões e agrupamentos
distintos dentro de um mesmo gráfico de dispersão.
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
# Carrega o conjunto de dados 'tips' de exemplo (gorjetas) nativo do Seaborn
tips = sns.load_dataset("tips")

# ===============================================
# INSPEÇÃO DE DADOS (Análise Exploratória Inicial)
# ===============================================
print("--- Visão Geral do DataFrame (Colunas e Primeiras Linhas) ---") 
print(tips.columns)                 # Exibe o nome de todas as colunas do DataFrame
print(tips.head())                  # Exibe as 5 primeiras linhas para inspeção inicial
print("-" * 30)

print("\n--- Estatísticas Descritivas (describe) ---") 
print(tips.describe())              # Gera estatísticas resumidas das colunas numéricas
print("-" * 30)

print("\n--- Tipos de Dados e Saúde do DF (info) ---") 
# Mostra tipos de dados, contagem de valores não-nulos e uso de memória
tips.info()
print("-" * 30)

# ===============================================
# VISUALIZAÇÃO DE DADOS (Scatter Plot com Hue via lmplot)
# ===============================================
# O lmplot cria um gráfico de dispersão e, por padrão, uma linha de regressão
scatter = sns.lmplot(
    x='total_bill',                 # Variável numérica para o eixo horizontal (Valor da conta)
    y='tip',                        # Variável numérica para o eixo vertical (Valor da gorjeta)
    data=tips,                      # Define o DataFrame de origem
    hue='sex',                      # Aplica cores distintas com base na categoria de gênero
    fit_reg=False                   # Desativa a linha de regressão linear para focar apenas nos pontos
)

# Adição de título ao gráfico através da estrutura FacetGrid do lmplot
scatter.fig.suptitle("Relação Conta x Gorjeta segmentada por Sexo (Hue)", y=1.05)

# ===============================================
# EXIBIÇÃO
# ===============================================
# Renderiza a visualização final
plt.show()