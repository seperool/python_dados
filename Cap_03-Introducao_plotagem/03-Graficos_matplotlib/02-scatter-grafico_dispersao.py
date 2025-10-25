#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 25 16:23:27 2025

@author: sergio
"""

# ----------------- Importação de Bibliotecas -----------------
import pandas as pd                      # Importa a biblioteca Pandas para manipulação de dados
import matplotlib.pyplot as plt          # Importa a biblioteca Matplotlib para a criação de gráficos
import seaborn as sns                    # Importa a biblioteca Seaborn para visualizações estatísticas (baseada em Matplotlib)

# ----------------- Carregamento e Inspeção dos Dados -----------------
tips = sns.load_dataset("tips")          # Carrega o conjunto de dados 'tips' (gorjetas) nativo do Seaborn
print(tips.head())                       # Imprime as primeiras 5 linhas do DataFrame para inspeção

# ----------------- Criação do Scatter Plot (Gráfico de Dispersão) -----------------
scatter_plot = plt.figure()              # Cria uma nova figura (tela/janela para o gráfico)
axes1 = scatter_plot.add_subplot(1,1,1)  # Adiciona um único subplot (1 linha, 1 coluna, 1º gráfico)
axes1.scatter(tips['total_bill'],tips['tip']) # Cria um gráfico de dispersão: 'total_bill' no eixo X e 'tip' no eixo Y
axes1.set_title("Scatterplot of Total Bill vs Tip") # Define o título do gráfico
axes1.set_xlabel("Total Bill")           # Define o rótulo do eixo X (Total da Conta)
axes1.set_ylabel("Tip")                  # Define o rótulo do eixo Y (Gorjeta)

# ----------------- Exibição do Gráfico -----------------
scatter_plot.show()                      # Exibe a figura (o gráfico)