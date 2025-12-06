#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Python para Análise Exploratória de Dados (EDA) e Visualização
usando Pandas, Matplotlib e Seaborn.

Created on Sat Dec 6 19:58:17 2025
@author: sergio

O foco é a criação de um **Gráfico de Barras (Bar Plot)** que visualiza uma métrica estatística
(definida por 'estimator', neste caso, o **desvio padrão**) de uma variável numérica ('total_bill')
agrupada por uma variável categórica ('time').

Função do barplot:
O **sns.barplot** calcula uma estatística (e.g., média, desvio padrão) para uma variável
numérica 'y', para cada categoria da variável 'x'.
1. A **altura da barra** representa a estatística agregada (aqui: Desvio Padrão do 'total_bill').
2. As **linhas pretas verticais** (barras de erro) representam a incerteza da estimativa (por padrão, o intervalo de confiança de 95%).
"""

# ===============================================
# IMPORTAÇÃO DE BIBLIOTECAS
# ===============================================
import pandas as pd                                # Alias 'pd' para manipulação e análise de dados (DataFrames)
import numpy as np                                 # Alias 'np' para operações numéricas, aqui usado para a função 'std' (desvio padrão)
import matplotlib.pyplot as plt                    # Alias 'plt' para plotagem de gráficos e ajustes de baixo nível
import seaborn as sns                              # Alias 'sns' para visualização estatística de alto nível

# ===============================================
# CARREGAMENTO DE DADOS
# ===============================================
# Carrega o conjunto de dados 'tips' de exemplo (gorjetas) do Seaborn
tips = sns.load_dataset("tips")                    

# ===============================================
# INSPEÇÃO DE DADOS (Análise Exploratória Inicial)
# ===============================================
print("--- Visão Geral do DataFrame (Colunas e Primeiras Linhas) ---") # Imprime um cabeçalho para seção
print(tips.columns)                                # Exibe o nome de todas as colunas
print(tips.head())                                 # Exibe as 5 primeiras linhas para inspeção rápida
print("-" * 30)                                    # Imprime um separador

print("\n--- Estatísticas Descritivas (describe) ---") # Imprime um cabeçalho para seção
print(tips.describe())                             # Gera estatísticas resumidas das colunas numéricas
print("-" * 30)                                    # Imprime um separador

print("\n--- Tipos de Dados e Saúde do DF (info) ---") # Imprime um cabeçalho para seção
print(tips.info())                                 # Mostra tipos de dados, contagem de valores não-nulos e uso de memória
print("-" * 30)                                    # Imprime um separador

# ===============================================
# VISUALIZAÇÃO DE DADOS (Bar Plot)
# ===============================================

# Cria a figura e o eixo do Matplotlib. 'bar' é o objeto Figure, 'ax' é o objeto Axes
bar, ax = plt.subplots()

# Cria o Gráfico de Barras
ax = sns.barplot(
  x='time',                                        # Variável categórica para o Eixo X (grupos: Dinner, Lunch)
  y='total_bill',                                  # Variável numérica para o Eixo Y
  data=tips,                                       # Especifica o DataFrame
  estimator=np.std                                 # Define a estatística a ser plotada no Eixo Y: Desvio Padrão (std)
) # O Desvio Padrão mede a dispersão dos valores 'total_bill' dentro de cada grupo 'time'

# Define o título do gráfico
ax.set_title("Bar plot of Standard Deviation of Total Bill by Time of Day")

# Define o rótulo do Eixo X
ax.set_xlabel("Time of day")

# Define o rótulo do Eixo Y (refletindo o uso do estimator=np.std)
ax.set_ylabel("Standard Deviation of Total Bill")

# Exibe o gráfico gerado
plt.show() # Necessário para renderizar o gráfico