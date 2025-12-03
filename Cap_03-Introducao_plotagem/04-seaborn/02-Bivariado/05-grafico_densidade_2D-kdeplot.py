#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Python para Análise Exploratória de Dados (EDA) e Visualização
usando Pandas, Matplotlib e Seaborn.

Created on Wed Dec 3 15:26:13 2025
@author: sergio

O foco é a criação de um **Gráfico de Estimativa de Densidade Kernel Bivariada (KDE 2D)**
utilizando a função sns.kdeplot em um ambiente Matplotlib pré-configurado.

Função do kdeplot (2D):
O **kdeplot** bivariado estima e visualiza a distribuição de probabilidade conjunta de duas variáveis contínuas (X e Y).
Ele usa contornos ou cores para indicar onde a densidade (concentração) de observações é maior.
É uma alternativa suave e contínua ao gráfico Hexbin ou ao Gráfico de Dispersão padrão.
"""

# ===============================================
# IMPORTAÇÃO DE BIBLIOTECAS
# ===============================================
import pandas as pd                                  # Alias 'pd' para manipulação e análise de dados (DataFrames)
import matplotlib.pyplot as plt                      # Alias 'plt' para plotagem de gráficos e ajustes de baixo nível
import seaborn as sns                                # Alias 'sns' para visualização estatística de alto nível

# ===============================================
# CARREGAMENTO DE DADOS
# ===============================================
# Carrega o conjunto de dados 'tips' de exemplo do Seaborn
tips = sns.load_dataset("tips")                      

# ===============================================
# INSPEÇÃO DE DADOS (Análise Exploratória Inicial)
# ===============================================
print("--- Visão Geral do DataFrame (Colunas e Primeiras Linhas) ---") # Imprime um cabeçalho
print(tips.columns)                                  # Exibe o nome de todas as colunas disponíveis
print(tips.head())                                   # Exibe as 5 primeiras linhas do DataFrame
print("-" * 30)                                      # Imprime um separador

print("\n--- Estatísticas Descritivas (describe) ---") # Imprime um cabeçalho
print(tips.describe())                               # Gera estatísticas resumidas das colunas numéricas
print("-" * 30)                                      # Imprime um separador

print("\n--- Tipos de Dados e Saúde do DF (info) ---") # Imprime um cabeçalho
print(tips.info())                                   # Mostra tipos de dados, contagem de nulos e uso de memória
print("-" * 30)                                      # Imprime um separador

# ===============================================
# VISUALIZAÇÃO DE DADOS (KDE Plot Bivariado)
# ===============================================

# Cria uma Figure e um conjunto de Axes (área de plotagem) no Matplotlib.
# 'kde' recebe o objeto Figure, e 'ax' recebe o objeto Axes.
kde, ax = plt.subplots() 

# Gera um gráfico de Estimativa de Densidade Kernel (KDE) 2D
ax = sns.kdeplot( 
  x=tips['total_bill'], # Variável para o Eixo X
  y=tips['tip'], # Variável para o Eixo Y (cria o gráfico bivariado)
  fill=True # Preenche as áreas sob os contornos de densidade com cores
)

# --- Customização Matplotlib/Seaborn ---

# Define o título do gráfico usando o objeto Axes
ax.set_title('Kernel Density Plot of Total Bill and Tip') 

# Define o rótulo do eixo X
ax.set_xlabel('Total Bill') 

# Define o rótulo do eixo Y
ax.set_ylabel('Tip') 

# Exibe o gráfico gerado
plt.show()