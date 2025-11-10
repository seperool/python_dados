#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Análise Exploratória e Visualização da Distribuição de Gorjetas (Tips).

Autor: sergio
Data de Criação: Sun Nov 9 18:42:51 2025

Este script carrega o conjunto de dados 'tips' do Seaborn, realiza uma
Análise Exploratória de Dados (EDA) inicial (colunas, head, describe, info)
e gera um gráfico de Estimativa de Densidade de Kernel (KDE) facetado
para visualizar a distribuição da conta total ('total_bill')
separada pelo período do dia ('time' - Almoço/Jantar).

Bibliotecas Requeridas:
- pandas
- matplotlib
- seaborn
"""

# ===============================================
# IMPORTAÇÃO DE BIBLIOTECAS
# ===============================================
import pandas as pd           # Manipulação e estruturação de dados (DataFrames).
import matplotlib.pyplot as plt # Plotagem de baixo nível e customização de gráficos.
import seaborn as sns         # Geração de gráficos estatísticos de alto nível.

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
print(tips.info())                # Resumo: tipos de dados e contagem de valores não-nulos.
print("-" * 30)

# ===============================================
# CRIAÇÃO DA VISUALIZAÇÃO (KDE FACETADO)
# ===============================================

# O objeto 'g' será um FacetGrid, retornado por sns.displot.
# Observação: Não use plt.subplots(), pois sns.displot gerencia a Figura internamente.

# Cria o gráfico KDE (Estimativa de Densidade de Kernel) facetado.
# kind='kde' para curva de densidade, col='time' para criar facetas por categoria.
g = sns.displot(data=tips,
                x='total_bill',
                kind='kde',
                col='time'
                )

# Customização do FacetGrid:

# 1. Título Geral: Define o título principal da Figura.
g.figure.suptitle("Total Bill Distribution by Time of Day", y=1.02)

# 2. Rótulos de Eixos: Aplica rótulos X e Y a todos os subgráficos.
g.set_axis_labels("Total Bill (USD)", "Frequency")

# 3. Títulos dos Subgráficos: Personaliza os títulos das facetas (ex: "Lunch Time").
g.set_titles(col_template="{col_name} Time")

# Exibe a visualização
plt.show()                        # Renderiza e exibe o gráfico.