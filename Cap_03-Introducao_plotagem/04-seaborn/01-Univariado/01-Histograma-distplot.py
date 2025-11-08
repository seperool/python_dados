#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Python para Análise Exploratória de Dados (EDA) e Visualização
usando Pandas e Seaborn.

Created on Thu Nov  6 17:11:13 2025
@author: sergio

O foco é demonstrar a funcionalidade da função **sns.distplot**.

Diferença entre distplot e Alternativas:
A função **sns.distplot** é considerada **obsoleta** (deprecated) e não deve ser usada em códigos novos.
Ela foi substituída por duas funções principais que oferecem maior clareza e flexibilidade:
1. `sns.histplot`: Função de "nível de Axes" (Axes-level) ideal para plotar um único histograma (e opcionalmente KDE) e oferece maior controle de customização do Matplotlib.
2. `sns.displot`: Função de "nível de Figure" (Figure-level) que unifica diferentes tipos de gráficos de distribuição (`kind='hist'`, `kind='kde'`) e é a única a suportar o *faceting* nativo (criação de múltiplos subgráficos com `col` ou `row`).
"""

# ===============================================
# IMPORTAÇÃO DE BIBLIOTECAS
# ===============================================
import pandas as pd           # Importa pandas para manipulação e análise de dados.
import matplotlib.pyplot as plt # Importa matplotlib para funções de plotagem e customização.
import seaborn as sns         # Importa seaborn para gráficos estatísticos de alto nível.

# ===============================================
# CARREGAMENTO DE DADOS
# ===============================================
tips = sns.load_dataset("tips") # Carrega o DataFrame de exemplo 'tips' do Seaborn.

# ===============================================
# INSPEÇÃO DE DADOS
# ===============================================
print("--- Visão Geral do DataFrame (columns e head) ---") # Título para a seção de visão geral.
print(tips.columns)           # Exibe os nomes das colunas do DataFrame.
print(tips.head())            # Exibe as 5 primeiras linhas para inspecionar a estrutura inicial.
print("-" * 30)               # Imprime uma linha separadora visual.

print("\n--- Estatísticas Descritivas (describe) ---") # Título para a seção de estatísticas.
print(tips.describe())        # Gera estatísticas descritivas para as colunas numéricas.
print("-" * 30)

print("\n--- Tipos de Dados e Valores Nulos (info) ---") # Título para a seção de saúde do DF.
print(tips.info())            # Verifica tipos de dados e a presença de valores nulos (missing values).
print("-" * 30)

# ===============================================
# CRIAÇÃO DA VISUALIZAÇÃO (HISTOGRAMA - DISTPLOT)
# ===============================================
# hist = plt.figure()           # Cria o objeto Figure (o contêiner/tela do gráfico).
# ax = hist.add_subplot(1, 1, 1) # Adiciona o objeto Axes (a área de plotagem do gráfico).
hist, ax = plt.subplots()     # Cria e desempacota a Figure (hist) e o Axes (ax) em uma linha.

# Cria e plota o Histograma no objeto 'ax' usando distplot
ax = sns.distplot(tips['total_bill'], kde=False) # Desenha o histograma da coluna 'total_bill'.

# Adiciona customizações ao plot usando o objeto 'ax'
ax.set_title("Total Bill Histogram") # Define o título principal do gráfico.
ax.set_xlabel("Total Bill")         # Define o rótulo do eixo X.
ax.set_ylabel("Frequency")          # Define o rótulo do eixo Y.

# Exibe a visualização
plt.show()                    # Exibe o gráfico configurado na tela.