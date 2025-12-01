#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Python para Análise Exploratória de Dados (EDA) e Visualização
usando Pandas e Seaborn.

Created on Mon Dec 1 20:15:46 2025
@author: sergio

O foco é a criação de um **Gráfico de Dispersão Bivariado de Cestas Hexagonais (Hexbin) com Histogramas Marginais**
utilizando a função sns.jointplot e o parâmetro kind="hex".

Função do jointplot (kind="hex"):
O **jointplot** no modo 'hex' cria uma figura com três componentes visuais:
1.  Um gráfico principal (central) que visualiza a relação bivariada usando **cestas hexagonais**. A cor/densidade do hexágono indica a frequência (contagem) de observações naquela área.
2.  Dois gráficos marginais (acima e à direita) que mostram a distribuição univariada (histogramas ou densidades) de cada uma das variáveis ('x' e 'y') independentemente.
Ele é ideal para analisar a distribuição conjunta e a densidade de dados quando há muitos pontos.
"""

# ===============================================
# IMPORTAÇÃO DE BIBLIOTECAS
# ===============================================
import pandas as pd                                  # Para manipulação e análise de dados (DataFrames)
import matplotlib.pyplot as plt                      # Para plotagem e customização de gráficos
import seaborn as sns                                # Para visualização estatística de alto nível

# ===============================================
# CARREGAMENTO DE DADOS
# ===============================================
tips = sns.load_dataset("tips")                      # Carrega o conjunto de dados 'tips' de exemplo do Seaborn

# ===============================================
# INSPEÇÃO DE DADOS (Análise Exploratória Inicial)
# ===============================================
print("--- Visão Geral do DataFrame (Colunas e Primeiras Linhas) ---") # Imprime um cabeçalho
print(tips.columns)                                  # Exibe o nome de todas as colunas
print(tips.head())                                   # Exibe as 5 primeiras linhas do DataFrame
print("-" * 30)                                      # Imprime um separador

print("\n--- Estatísticas Descritivas (describe) ---") # Imprime um cabeçalho
print(tips.describe())                               # Gera estatísticas resumidas das colunas numéricas
print("-" * 30)                                      # Imprime um separador

print("\n--- Tipos de Dados e Saúde do DF (info) ---") # Imprime um cabeçalho
print(tips.info())                                   # Mostra tipos de dados, contagem de nulos e uso de memória
print("-" * 30)                                      # Imprime um separador

# ===============================================
# VISUALIZAÇÃO DE DADOS (Gráfico Hexbin Bivariado e Marginal)
# ===============================================

hexbin = sns.jointplot(                              # Cria o Gráfico de Junção (Joint Plot)
  x="total_bill",                                    # Define a variável para o Eixo X
  y="tip",                                           # Define a variável para o Eixo Y
  data=tips,                                         # Especifica o DataFrame a ser usado
  kind="hex"                                         # Define o tipo de gráfico como Hexbin
)

hexbin.set_axis_labels(                              # Define os Rótulos dos Eixos
  xlabel='Total Bill',                               # Rótulo para o Eixo X
  ylabel='Tip'                                       # Rótulo para o Eixo Y
)

hexbin.fig.suptitle(                                 # Adiciona um Título Geral à Figura
  'Hexbin Joint Plot of Total Bill and Tip',         # Texto do título
  fontsize=10,                                       # Define o tamanho da fonte
  y=1.03                                             # Ajusta a posição vertical do título
)

plt.show()                                           # Exibe o gráfico gerado