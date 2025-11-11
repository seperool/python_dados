#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Análise e Visualização da Distribuição Unidimensional (Distplot).

Autor: sergio
Data de Criação: Tue Nov 11 00:48:52 2025

Este script carrega o conjunto de dados 'tips' e gera uma visualização
combinada da distribuição da conta total ('total_bill') usando a função
'distplot' do Seaborn, que inclui por padrão:
1. Histograma.
2. Estimativa de Densidade de Kernel (KDE).
3. Rug Plot (marcas individuais no eixo X), ativado por rug=True.

Bibliotecas Requeridas:
- pandas
- matplotlib
- seaborn
"""

# ===============================================
# IMPORTAÇÃO DE BIBLIOTECAS
# ===============================================
import pandas as pd              # Manipulação e estruturação de dados (DataFrames).
import matplotlib.pyplot as plt  # Plotagem de baixo nível e customização de gráficos.
import seaborn as sns            # Geração de gráficos estatísticos de alto nível.

# ===============================================
# CARREGAMENTO DE DADOS
# ===============================================
tips = sns.load_dataset("tips") # Carrega o conjunto de dados 'tips' do Seaborn.

# ===============================================
# INSPEÇÃO DE DADOS (EDA Inicial)
# ===============================================
print("--- Visão Geral do DataFrame ---")
print(tips.columns)               # Exibe os nomes das colunas.
print(tips.head())                # Exibe as 5 primeiras linhas.
print("-" * 30)

print("\n--- Estatísticas Descritivas ---")
print(tips.describe())            # Gera estatísticas resumidas para colunas numéricas.
print("-" * 30)

print("\n--- Tipos de Dados e Não-Nulos ---")
# O output de tips.info() é impresso diretamente, mas a chamada retorna None.
# A impressão acima é mantida para respeitar a estrutura.
tips.info()
print("-" * 30)

# ===============================================
# CRIAÇÃO DA VISUALIZAÇÃO (DISTPLOT com RUG PLOT)
# ===============================================

# Cria uma figura (fig) e um único eixo/subgráfico (ax) no Matplotlib.
# Foi renomeado de 'hist_den_rug' para 'fig' para convenção, mantendo o ax.
hist_den_rug, ax = plt.subplots()

# Gera o gráfico de distribuição (distplot) no eixo 'ax'.
# Por padrão, inclui Histograma e KDE. O parâmetro rug=True adiciona o Rug Plot.
ax = sns.distplot(
             tips["total_bill"], # Variável contínua ('total_bill') para o eixo X.
             rug=True            # Adiciona um "Rug Plot" na parte inferior do eixo X.
             )

# Customização do Eixo (Axes):
ax.set_title("Total Bill Histogram with Density and Rug Plot") # Define o título do subgráfico.
ax.set_xlabel("Total Bill") # Define o rótulo do eixo X.
ax.set_ylabel("Density")    # Define o rótulo do eixo Y.

# Exibe a visualização
plt.show() # Renderiza e exibe o gráfico.