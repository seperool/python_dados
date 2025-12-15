#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Python para Análise Exploratória de Dados (EDA) e Visualização
usando Pandas, Matplotlib e Seaborn.

Created on Mon Dec 15 01:31:28 2025
@author: sergio

Este script carrega o conjunto de dados 'tips' e realiza uma inspeção inicial.
O foco principal é a **Visualização de Dados** através da criação de um
**Gráfico de Dispersão (Scatter Plot)** customizado usando o Seaborn.

O Gráfico de Dispersão (via sns.lmplot) é útil para visualizar a relação
entre duas variáveis quantitativas (total_bill e tip), usando cores (hue)
para mapear uma variável categórica (sex).
"""

# ===============================================
# IMPORTAÇÃO DE BIBLIOTECAS
# ===============================================
import pandas as pd                             # Alias 'pd' para manipulação e análise de dados (DataFrames)
import numpy as np                              # Alias 'np' para operações numéricas (mantido, embora não usado diretamente)
import matplotlib.pyplot as plt                 # Alias 'plt' para plotagem de gráficos e ajustes de baixo nível
import seaborn as sns                           # Alias 'sns' para visualização estatística de alto nível

# ===============================================
# CARREGAMENTO DE DADOS
# ===============================================
# Carrega o conjunto de dados 'tips' de exemplo (gorjetas) diretamente do Seaborn
tips = sns.load_dataset("tips")                 # Carrega o DataFrame 'tips' (conta total, gorjeta, gênero, etc.)

# ===============================================
# INSPEÇÃO DE DADOS (Análise Exploratória Inicial)
# ===============================================
print("--- Visão Geral do DataFrame (Colunas e Primeiras Linhas) ---") # Imprime um cabeçalho para seção
print(tips.columns)                             # Exibe o nome de todas as colunas do DataFrame
print(tips.head())                              # Exibe as 5 primeiras linhas para inspeção rápida da estrutura
print("-" * 30)                                 # Imprime um separador (30 hífens)

print("\n--- Estatísticas Descritivas (describe) ---") # Imprime um cabeçalho para seção
print(tips.describe())                          # Gera estatísticas resumidas das colunas numéricas (contagem, média, desvio padrão, quartis)
print("-" * 30)                                 # Imprime um separador (30 hífens)

print("\n--- Tipos de Dados e Saúde do DF (info) ---") # Imprime um cabeçalho para seção
tips.info()                                     # Mostra tipos de dados, contagem de valores não-nulos e uso de memória
print("-" * 30)                                 # Imprime um separador (30 hífens)

# ===============================================
# VISUALIZAÇÃO DE DADOS (Gráfico de Dispersão - lmplot)
# ===============================================
scatter = sns.lmplot(                           # Cria um gráfico de dispersão com base em FacetGrid
  x='total_bill',                               # Variável para o eixo X (Valor total da conta)
  y='tip',                                      # Variável para o eixo Y (Valor da gorjeta)
  data=tips,                                    # Define o DataFrame de origem
  fit_reg=False,                                # Desativa a linha de regressão linear (apenas pontos)
  hue='sex',                                    # Variável categórica para mapear cores (Diferencia por Gênero)
  scatter_kws={'s': 80}                         # Argumentos passados para plt.scatter: define o tamanho dos pontos como 80
)                                               # Cria o objeto FacetGrid/Gráfico de Dispersão

# Exibe o gráfico gerado.
plt.show()                                      # Renderiza a visualização final do Scatter Plot