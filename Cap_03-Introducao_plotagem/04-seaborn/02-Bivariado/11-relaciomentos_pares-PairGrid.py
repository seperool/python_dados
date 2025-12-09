#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Python para Análise Exploratória de Dados (EDA) e Visualização
usando Pandas, Matplotlib e Seaborn.

Created on Tue Dec 9 13:24:54 2025
@author: sergio

O foco é a criação e customização de uma **PairGrid (Grade de Pares)**,
que permite mapear diferentes tipos de gráficos (regressão, KDE, distribuição)
para as diferentes seções da grade (superior, inferior e diagonal).

Classes e Funções principais:
1. **sns.PairGrid**: Cria a estrutura base da matriz (grade) sem preencher os gráficos.
2. **map_upper**: Aplica um tipo de gráfico (e.g., sns.regplot) aos gráficos **acima da diagonal**.
3. **map_lower**: Aplica um tipo de gráfico (e.g., sns.kdeplot) aos gráficos **abaixo da diagonal**.
4. **map_diag**: Aplica um tipo de gráfico (e.g., sns.distplot) aos gráficos na **diagonal**.
"""

# ===============================================
# IMPORTAÇÃO DE BIBLIOTECAS
# ===============================================
import pandas as pd # Alias 'pd' para manipulação e análise de dados (DataFrames)
import numpy as np # Alias 'np' para operações numéricas (mantido, embora não usado diretamente)
import matplotlib.pyplot as plt # Alias 'plt' para plotagem de gráficos e ajustes de baixo nível
import seaborn as sns # Alias 'sns' para visualização estatística de alto nível

# ===============================================
# CARREGAMENTO DE DADOS
# ===============================================
# Carrega o conjunto de dados 'tips' de exemplo (gorjetas) diretamente do Seaborn
tips = sns.load_dataset("tips")

# ===============================================
# INSPEÇÃO DE DADOS (Análise Exploratória Inicial)
# ===============================================
print("--- Visão Geral do DataFrame (Colunas e Primeiras Linhas) ---") # Imprime um cabeçalho para seção
print(tips.columns) # Exibe o nome de todas as colunas do DataFrame
print(tips.head()) # Exibe as 5 primeiras linhas para inspeção rápida da estrutura
print("-" * 30) # Imprime um separador

print("\n--- Estatísticas Descritivas (describe) ---") # Imprime um cabeçalho para seção
print(tips.describe()) # Gera estatísticas resumidas das colunas numéricas (contagem, média, desvio padrão, quartis)
print("-" * 30) # Imprime um separador

print("\n--- Tipos de Dados e Saúde do DF (info) ---") # Imprime um cabeçalho para seção
# Mostra tipos de dados, contagem de valores não-nulos e uso de memória
tips.info()
print("-" * 30) # Imprime um separador

# ===============================================
# VISUALIZAÇÃO DE DADOS (PairGrid Customizado)
# ===============================================

# 1. Inicializa a grade: Cria a estrutura vazia da matriz de gráficos para todas as colunas numéricas
pair_grid = sns.PairGrid(tips) 

# 2. Mapeia a seção SUPERIOR da grade:
# Usa sns.regplot (Regressão Linear e Dispersão) para mostrar a relação e linha de ajuste
# podemos usar plt.scatter em vez de sns.regplot (Comentário: regplot é preferível para regressão)
pair_grid = pair_grid.map_upper(sns.regplot)

# 3. Mapeia a seção INFERIOR da grade:
# Usa sns.kdeplot (Kernel Density Estimate) para visualizar a densidade bivariada entre os pares de variáveis
pair_grid = pair_grid.map_lower(sns.kdeplot)

# 4. Mapeia a DIAGONAL da grade:
# Usa sns.distplot (Distribuição) para mostrar a distribuição univariada de cada variável.
# 'rug=True' adiciona marcas ao longo do eixo para mostrar a localização de cada observação.
pair_grid = pair_grid.map_diag(sns.histplot, kde=True, bins=10) # Alterado de distplot (depreciado) para histplot

# Exibe o gráfico gerado.
plt.show() #