#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Python para Análise Exploratória de Dados (EDA) e Visualização
usando Pandas, Matplotlib e Seaborn.

Created on Thu Dec 18 15:50:30 2025
@author: sergio

Este script utiliza a biblioteca Seaborn para demonstrar a personalização de 
gráficos de dispersão. O foco principal é o ajuste estético dos marcadores, 
utilizando o argumento 'markers' para alterar a forma dos pontos (ex: círculos 
e X) e o dicionário 'scatter_kws' para controlar o tamanho (s) dos elementos 
plotados.
"""

# ===============================================
# IMPORTAÇÃO DE BIBLIOTECAS
# ===============================================
import pandas as pd                      # Alias 'pd' para manipulação e análise de dados (DataFrames)
import numpy as np                      # Alias 'np' para operações numéricas (mantido para compatibilidade)
import matplotlib.pyplot as plt          # Alias 'plt' para plotagem de gráficos e ajustes de baixo nível
import seaborn as sns                    # Alias 'sns' para visualização estatística de alto nível

# ===============================================
# CARREGAMENTO DE DADOS
# ===============================================
# Carrega o conjunto de dados 'tips' de exemplo (gorjetas) diretamente do Seaborn
tips = sns.load_dataset("tips")          # Carrega o DataFrame 'tips' (conta total, gorjeta, gênero, etc.)

# ===============================================
# INSPEÇÃO DE DADOS (Análise Exploratória Inicial)
# ===============================================
print("--- Visão Geral do DataFrame (Colunas e Primeiras Linhas) ---")
print(tips.columns)                      # Exibe o nome de todas as colunas do DataFrame
print(tips.head())                       # Exibe as 5 primeiras linhas para inspeção rápida da estrutura
print("-" * 30)

print("\n--- Estatísticas Descritivas (describe) ---")
print(tips.describe())                   # Gera estatísticas resumidas das colunas numéricas
print("-" * 30)

print("\n--- Tipos de Dados e Saúde do DF (info) ---")
tips.info()                              # Mostra tipos de dados, contagem de valores não-nulos e memória
print("-" * 30)

# ===============================================
# VISUALIZAÇÃO DE DADOS (Gráfico de Dispersão - lmplot)
# ===============================================

scatter = sns.lmplot(                    # Cria um gráfico de dispersão com base em FacetGrid
    x='total_bill',                      # Variável para o eixo X (Valor total da conta)
    y='tip',                             # Variável para o eixo Y (Valor da gorjeta)
    data=tips,                           # Define o DataFrame de origem
    fit_reg=False,                       # Desativa a linha de regressão linear (foco apenas nos pontos)
    hue='sex',                           # Variável categórica para mapear cores (Diferencia por Gênero)
    markers=['o', 'x'],                  # Define as FORMAS: 'o' (círculo) para a primeira categoria, 'x' para a segunda
    scatter_kws={'s': 80}                # Define o TAMANHO: Argumento 's' (size) ajusta a área dos pontos para 80
)                                        # Cria o objeto FacetGrid/Gráfico de Dispersão

# Ajustes finais de layout e exibição
plt.title("Dispersão: Conta vs Gorjeta (Formas Customizadas)")
plt.show()                               # Renderiza a visualização final do Scatter Plot