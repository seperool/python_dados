#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Análise e Visualização da Distribuição Categórica (Countplot).

Autor: sergio
Data de Criação: Tue Nov 11 01:00:14 2025

Este script carrega o conjunto de dados 'tips' e gera um Gráfico de Contagem
(Countplot) usando a função 'countplot' do Seaborn para visualizar a frequência
de visitas por dia da semana ('day').

O Countplot é a forma categórica do histograma, mostrando a contagem absoluta
de observações em cada categoria.

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
# Resumo dos tipos de dados e contagem de valores não-nulos.
tips.info()
print("-" * 30)

# ===============================================
# CRIAÇÃO DA VISUALIZAÇÃO (COUNTPLOT)
# ===============================================

# Cria uma figura (fig) e um único eixo/subgráfico (ax) no Matplotlib.
# Foi renomeado de 'count' para 'fig' para convenção, mantendo o ax.
fig, ax = plt.subplots()

# Gera o Gráfico de Contagem (countplot) no eixo 'ax'.
ax = sns.countplot(
             x='day',            # Variável categórica para o eixo X (Dia da Semana).
             data=tips           # DataFrame a ser utilizado.
             )

# Customização do Eixo (Axes):
ax.set_title("Frequência de Visitas por Dia da Semana") # Define o título do subgráfico.
ax.set_xlabel("Dia da Semana") # Define o rótulo do eixo X.
ax.set_ylabel("Contagem (Frequência)") # Define o rótulo do eixo Y.

# Exibe a visualização
plt.show() # Renderiza e exibe o gráfico.