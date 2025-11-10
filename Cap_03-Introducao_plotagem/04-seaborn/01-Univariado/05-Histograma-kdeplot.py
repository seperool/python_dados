#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Análise e Visualização da Distribuição Unidimensional.

Autor: sergio
Data de Criação: Sun Nov 9 19:08:51 2025

Este script carrega o conjunto de dados 'tips' e, após uma Análise
Exploratória de Dados (EDA) inicial (colunas, head, describe, info),
gera um gráfico de Estimativa de Densidade de Kernel (KDE) unidimensional
para visualizar a distribuição da conta total ('total_bill').

O gráfico utiliza a sintaxe Matplotlib (plt.subplots) combinada com
a função 'kdeplot' do Seaborn para plotagem.

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
# CRIAÇÃO DA VISUALIZAÇÃO (KDE UNIDIMENSIONAL)
# ===============================================

# Cria uma figura (fig) e um único eixo/subgráfico (ax) no Matplotlib.
fig, ax = plt.subplots()

# Gera o gráfico KDE (Estimativa de Densidade de Kernel) no eixo 'ax'.
ax = sns.kdeplot(
            tips['total_bill'], # Variável contínua ('total_bill') para o eixo X.
            fill=True,      # Preenche a área sob a curva.
            alpha=0.5,      # Define a transparência do preenchimento.
            linewidth=2     # Define a espessura da linha da curva.
           )

# Customização do Eixo (Axes):
ax.set_title("Estimativa de Densidade de Kernel da Conta Total") # Define o título do subgráfico.
ax.set_xlabel("Total Bill") # Define o rótulo do eixo X.
ax.set_ylabel("Density")    # Define o rótulo do eixo Y.

# Exibe a visualização
plt.show() # Renderiza e exibe o gráfico.