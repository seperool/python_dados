#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 25 16:26:42 2025

@author: sergio
"""

# ----------------- Importação de Bibliotecas -----------------
import pandas as pd                      # Importa a biblioteca Pandas para manipulação de dados
import matplotlib.pyplot as plt          # Importa a biblioteca Matplotlib para a criação de gráficos
import seaborn as sns                    # Importa a biblioteca Seaborn para visualizações estatísticas (baseada em Matplotlib)

# ----------------- Carregamento e Inspeção dos Dados -----------------
tips = sns.load_dataset("tips")          # Carrega o conjunto de dados 'tips' (gorjetas) nativo do Seaborn
print(tips.head())                       # Imprime as primeiras 5 linhas do DataFrame para inspeção

# ----------------- Criação do Boxplot (Gráfico de Caixa) -----------------
boxplot = plt.figure()                   # Cria uma nova figura (tela/janela para o gráfico)
axes1 = boxplot.add_subplot(1,1,1)       # Adiciona um único subplot (1 linha, 1 coluna, 1º gráfico)
axes1.boxplot(                           # Cria o gráfico de caixa
  # O primeiro argumento de um gráfico de caixa é o dado,
  # pois estamos plotando várias porções de dados;
  # temos que colocar cada porção de dados em uma lista
  [tips[tips['sex'] == 'Female']['tip'], # Dados das gorjetas para o sexo 'Female'
  tips[tips['sex'] == 'Male']['tip']],   # Dados das gorjetas para o sexo 'Male'
  # Podemos então passar um parâmetro labels opcional
  # para especificar um rótulo aos dados que passamos
  labels = ['Female','Male']             # Define os rótulos para cada caixa (Female e Male)
)
axes1.set_xlabel('Sex')                  # Define o rótulo do eixo X (Sexo)
axes1.set_ylabel('Tip')                  # Define o rótulo do eixo Y (Gorjeta)
axes1.set_title('Boxplot of Tips by Sex') # Define o título do gráfico

# ----------------- Exibição do Gráfico -----------------
boxplot.show()                           # Exibe a figura (o gráfico)