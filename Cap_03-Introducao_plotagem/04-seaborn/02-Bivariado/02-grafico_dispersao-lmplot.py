#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Python para Análise Exploratória de Dados (EDA) e Visualização
usando Pandas e Seaborn.

Created on Fri Nov 28 12:30:16 2025
@author: sergio

O foco é a criação de um Gráfico de Regressão Linear com Múltiplos Painéis (Facet Grids)
utilizando sns.lmplot.

Função do lmplot:
O **lmplot** (Linear Model Plot) é uma função de "nível de Figura" do Seaborn
que combina `regplot` e `FacetGrid`. Ele plota dados de dispersão com uma linha
de regressão linear, mas sua principal vantagem é a facilidade em criar
**múltiplos gráficos** (facetas) a partir de variáveis categóricas (usando 'col'
e/ou 'row'), permitindo analisar a relação linear de forma mais detalhada dentro
de subgrupos dos dados.
"""

# ===============================================
# IMPORTAÇÃO DE BIBLIOTECAS
# ===============================================
import pandas as pd # Para manipulação e análise de dados (DataFrames)
import matplotlib.pyplot as plt # Para plotagem e customização de gráficos
import seaborn as sns # Para visualização estatística de alto nível

# ===============================================
# CARREGAMENTO DE DADOS
# ===============================================
tips = sns.load_dataset("tips") # Carrega o conjunto de dados 'tips' de exemplo do Seaborn

# ===============================================
# INSPEÇÃO DE DADOS (Análise Exploratória Inicial)
# ===============================================
print("--- Visão Geral do DataFrame (Colunas e Primeiras Linhas) ---") # Imprime um cabeçalho
print(tips.columns) # Exibe o nome de todas as colunas
print(tips.head()) # Exibe as 5 primeiras linhas do DataFrame
print("-" * 30) # Imprime um separador

print("\n--- Estatísticas Descritivas (describe) ---") # Imprime um cabeçalho
print(tips.describe()) # Gera estatísticas resumidas das colunas numéricas
print("-" * 30) # Imprime um separador

print("\n--- Tipos de Dados e Saúde do DF (info) ---") # Imprime um cabeçalho
print(tips.info()) # Mostra tipos de dados, contagem de nulos e uso de memória
print("-" * 30) # Imprime um separador

# ===============================================
# VISUALIZAÇÃO DE DADOS (Gráfico de Regressão com Facetas)
# ==============================================
# O lmplot retorna um objeto FacetGrid (fig), que lida com a figura e os eixos
fig = sns.lmplot( # Cria o gráfico de dispersão com regressão em subplots
    x='total_bill', # Variável no eixo X (Conta Total)
    y='tip', # Variável no eixo Y (Gorjeta)
    data=tips, # DataFrame a ser usado
    )

# Configura o título da Figura (funciona no nível do objeto FacetGrid)
fig.fig.suptitle("Linear Model Plot of Total Bill vs Tip")
fig.set_axis_labels("Total Bill ($)", "Tip ($)") # Configura os rótulos dos eixos para todas as facetas

plt.show() # Exibe a Figura (Facets Grid) gerada