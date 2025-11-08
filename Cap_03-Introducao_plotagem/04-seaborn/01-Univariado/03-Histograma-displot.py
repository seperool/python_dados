#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Python para Análise Exploratória de Dados (EDA) e Visualização
usando Pandas e Seaborn.

Autor: sergio
Data de Criação: Sat Nov 8 01:58:09 2025

O foco é demonstrar a criação de um Histograma Facetado (displot)
e a customização do objeto FacetGrid retornado.

O **displot** é uma função de alto nível que unifica a plotagem de distribuições.
Ele substitui o obsoleto `distplot` e adiciona o recurso de **faceting** (subgráficos com `col` ou `row`),
o que o diferencia do `histplot` (função de nível de Axes focada apenas em histogramas, sem faceting nativo).
"""

# ===============================================
# IMPORTAÇÃO DE BIBLIOTECAS
# ===============================================
import pandas as pd             # Importa pandas para manipulação e estruturação de dados (DataFrames).
import matplotlib.pyplot as plt # Importa Matplotlib para funcionalidades de plotagem de baixo nível e customização.
import seaborn as sns           # Importa Seaborn, biblioteca de alto nível para gráficos estatísticos.

# ===============================================
# CARREGAMENTO DE DADOS
# ===============================================
tips = sns.load_dataset("tips") # Carrega o conjunto de dados de exemplo 'tips' (Gorjetas) do Seaborn.

# ===============================================
# INSPEÇÃO DE DADOS (Análise Exploratória Inicial)
# ===============================================
print("--- Visão Geral do DataFrame (Colunas e Primeiras Linhas) ---") # Título para a seção.
print(tips.columns)               # Exibe os nomes das colunas disponíveis no DataFrame.
print(tips.head())                # Exibe as 5 primeiras linhas para verificar a estrutura e o formato dos dados.
print("-" * 30)                   # Separador visual.

print("\n--- Estatísticas Descritivas (describe) ---") # Título da seção.
print(tips.describe())            # Gera estatísticas resumidas para as colunas numéricas.
print("-" * 30)

print("\n--- Tipos de Dados e Saúde do DF (info) ---") # Título da seção.
print(tips.info())                # Fornece um resumo do DataFrame (tipos de dados e valores não-nulos).
print("-" * 30)

# ===============================================
# CRIAÇÃO DA VISUALIZAÇÃO (HISTOGRAMA FACETADO)
# ===============================================

# O objeto FacetGrid (g) é retornado ao usar 'col' ou 'row'.
# RAZÃO: sns.displot já cria sua própria Figure e retorna o FacetGrid (g), não o Axes (ax).
# Usar plt.subplots() aqui criaria um Axes que seria ignorado e não usado.

# Cria o Histograma Facetado usando sns.displot.
# O parâmetro 'kind' define o tipo de gráfico:
# - kind='hist': Histograma (padrão)
# - kind='kde': Estimativa de Densidade de Kernel (curvas suaves)
g = sns.displot(data=tips,          # Passa o DataFrame.
                x='total_bill',     # Variável contínua para o eixo X.
                kind='hist',
                col='time'          # Variável categórica para criar subgráficos em colunas (Faceting).
                )

# Customização do FacetGrid:

# 1. Título Geral (Supra-título): Usa o objeto Figure do FacetGrid para definir o título geral.
#    O parâmetro y=1.02 move o título ligeiramente para cima.
g.figure.suptitle("Total Bill Distribution by Time of Day", y=1.02)

# 2. Rótulos de Eixos: Aplica os rótulos X e Y a todos os subgráficos da grade.
g.set_axis_labels("Total Bill (USD)", "Frequency")

# 3. Títulos dos Subgráficos (Facetas): Personaliza os títulos padrão das colunas ('time = Lunch', etc.).
#    {col_name} é um placeholder para o valor da coluna 'time'.
g.set_titles(col_template="{col_name} Time")

# Exibe a visualização
plt.show()                        # Renderiza e exibe o gráfico.