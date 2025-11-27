#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Python para Análise Exploratória de Dados (EDA) e Visualização
usando Pandas e Seaborn.

Created on Thu Nov 27 11:40:13 2025
@author: sergio

O foco é a criação de um Gráfico de Dispersão Bivariado com Linha de Regressão
utilizando sns.regplot.

Função do regplot:
O **regplot** (Regression Plot) plota dados de dispersão e adiciona automaticamente
uma linha de regressão linear para ajudar a visualizar a relação linear entre
duas variáveis numéricas (neste caso, 'total_bill' e 'tip'). Ele também exibe
uma banda de confiança em torno da linha. É uma função de "nível de Axes" do Seaborn.
"""

# ===============================================
# IMPORTAÇÃO DE BIBLIOTECAS
# ===============================================
import pandas as pd                                # Para manipulação e análise de dados (DataFrames)
import matplotlib.pyplot as plt                    # Para plotagem e customização de gráficos
import seaborn as sns                              # Para visualização estatística de alto nível

# ===============================================
# CARREGAMENTO DE DADOS
# ===============================================
tips = sns.load_dataset("tips")                    # Carrega o conjunto de dados 'tips' de exemplo do Seaborn

# ===============================================
# INSPEÇÃO DE DADOS (Análise Exploratória Inicial)
# ===============================================
print("--- Visão Geral do DataFrame (Colunas e Primeiras Linhas) ---") # Imprime um cabeçalho
print(tips.columns)                                # Exibe o nome de todas as colunas
print(tips.head())                                 # Exibe as 5 primeiras linhas do DataFrame
print("-" * 30)                                    # Imprime um separador

print("\n--- Estatísticas Descritivas (describe) ---") # Imprime um cabeçalho
print(tips.describe())                             # Gera estatísticas resumidas das colunas numéricas
print("-" * 30)                                    # Imprime um separador

print("\n--- Tipos de Dados e Saúde do DF (info) ---") # Imprime um cabeçalho
print(tips.info())                                 # Mostra tipos de dados, contagem de nulos e uso de memória
print("-" * 30)                                    # Imprime um separador

# ===============================================
# VISUALIZAÇÃO DE DADOS (Gráfico de Dispersão com Regressão)
# ==============================================
scatter, ax = plt.subplots()                       # Cria a figura (scatter) e os eixos (ax)
ax = sns.regplot(                                  # Plota o gráfico de dispersão com linha de regressão
  x='total_bill',                                  # Variável no eixo X (Conta Total)
  y='tip',                                         # Variável no eixo Y (Gorjeta)
  data=tips)                                       # DataFrame a ser usado
ax.set_title("Scatterplot of Total Bill and Tip")  # Define o título do gráfico
ax.set_xlabel("Total Bill")                        # Define o rótulo do eixo X
ax.set_ylabel("Tip")                               # Define o rótulo do eixo Y

plt.show()                                         # Exibe o gráfico gerado