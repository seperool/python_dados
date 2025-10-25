#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 25 16:06:48 2025

@author: sergio
"""

# ----------------- Importação de Bibliotecas -----------------
import pandas as pd                      # Importa a biblioteca Pandas para manipulação de dados
import matplotlib.pyplot as plt          # Importa a biblioteca Matplotlib para a criação de gráficos
import seaborn as sns                    # Importa a biblioteca Seaborn para visualizações estatísticas (baseada em Matplotlib)

# ----------------- Carregamento e Inspeção dos Dados -----------------
tips = sns.load_dataset("tips")          # Carrega o conjunto de dados 'tips' (gorjetas) nativo do Seaborn
print(tips.head())                       # Imprime as primeiras 5 linhas do DataFrame para inspeção

# ----------------- Criação do Histograma (Matplotlib Puro) -----------------
fig = plt.figure()                       # Cria uma nova figura (tela/janela para o gráfico)
axes1 = fig.add_subplot(1,1,1)           # Adiciona um único subplot (1 linha, 1 coluna, 1º gráfico) à figura
axes1.hist(tips['total_bill'],bins=10)   # Cria um histograma da coluna 'total_bill' com 10 barras (bins)
axes1.set_title("Histogram of Total Bill") # Define o título do gráfico
axes1.set_xlabel("Frequency")            # Define o rótulo do eixo X (Frequência)
axes1.set_ylabel("Total Bill")           # Define o rótulo do eixo Y (Total da Conta)

# ----------------- Exibição do Gráfico -----------------
fig.show()                               # Exibe a figura (o gráfico)