#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Python para Análise Exploratória de Dados (EDA) e Visualização
usando Pandas e Seaborn.

Created on Sat Nov 29 17:26:04 2025
@author: sergio

O foco é a criação de um **Gráfico de Dispersão Bivariado com Histogramas Marginais**
utilizando a função sns.jointplot.

Função do jointplot:
O **jointplot** cria uma figura com três componentes visuais:
1.  Um gráfico principal (central) que visualiza a relação bivariada (Ex: dispersão)
    entre as variáveis definidas em 'x' e 'y'.
2.  Dois gráficos marginais (acima e à direita) que mostram a distribuição univariada
    (Ex: histogramas ou densidades) de cada uma das variáveis ('x' e 'y')
    independentemente.
Ele é ideal para analisar a distribuição conjunta e individual dos dados.
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
# VISUALIZAÇÃO DE DADOS (Gráfico Bivariado e Marginal)
# ===============================================
joint = sns.jointplot( # Cria a figura com o gráfico principal e os marginais (retorna um objeto JointGrid)
    x='total_bill', # Variável no eixo X (Conta Total)
    y='tip', # Variável no eixo Y (Gorjeta)
    data=tips, # DataFrame a ser usado
    height=5 # Define o tamanho da figura (em polegadas quadradas, se 'ratio' não for usado)
    )

# Configura os rótulos dos eixos X e Y
joint.set_axis_labels(
    xlabel='Total Bill', # Rótulo para o eixo X
    ylabel='Tip') # Rótulo para o eixo Y

# Configura o título geral da figura (objeto 'fig' dentro do JointGrid)
joint.fig.suptitle('Join Plot of Total Bill and Tip',
    fontsize=10, # Define o tamanho da fonte do título
    y=1.03) # Ajusta a posição vertical do título para ficar acima do gráfico

plt.show() # Exibe a Figura gerada