#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Matriz de Facetas Bidimensional para Dados Multivariados
Este programa utiliza o FacetGrid para cruzar cinco variáveis do dataset 'tips':
1. total_bill (X) e tip (Y) - Relação numérica
2. time (col) - Comparação horizontal (Almoço/Jantar)
3. smoker (row) - Comparação vertical (Fumante/Não Fumante)
4. sex (hue) - Diferenciação por cores dentro de cada quadrante

Tópicos: Matriz de facetas (row/col), Escalonamento (height/aspect).
Created on Mon Dec 22 10:51:40 2025
@author: sergio
"""

# ===============================================
# IMPORTAÇÃO DE BIBLIOTECAS
# ===============================================
import pandas as pd              # Manipulação e análise de dados estruturados
import numpy as np               # Computação científica e operações vetoriais
import matplotlib.pyplot as plt    # Interface de plotagem de baixo nível para ajustes finos
import seaborn as sns            # Biblioteca de visualização estatística de alto nível

# ===============================================
# CARREGAMENTO DE DADOS
# ===============================================
# O dataset 'tips' contém dados de gorjetas e variáveis comportamentais
tips = sns.load_dataset("tips") 

# ===============================================
# INSPEÇÃO DE DADOS (Análise Exploratória Inicial)
# ===============================================
print("--- Visão Geral do DataFrame ---")
print(tips.head())              # Exibe as primeiras linhas
print("-" * 30)

print("\n--- Estatísticas Descritivas ---")
print(tips.describe())          # Resumo estatístico das variáveis numéricas
print("-" * 30)

# ===============================================
# VISUALIZAÇÃO MULTIVARIADA (Matriz de Facetas)
# ===============================================
# A inicialização define a estrutura lógica da grade (rows, cols, hue)
facet = sns.FacetGrid(
    tips,              # Fonte dos dados
    col='time',        # Variável categórica para as COLUNAS (Eixo horizontal da grade)
    row='smoker',      # Variável categórica para as LINHAS (Eixo vertical da grade)
    hue='sex',         # Variável categórica para as CORES (Subdivisão interna)
    height=2.5,        # Altura de cada subplot individual (em polegadas)
    aspect=1           # Proporção largura/altura (1.0 = gráfico quadrado)
)

# 

# O mapeamento aplica a função de dispersão em todos os quadrantes da matriz
facet.map(
    plt.scatter,       # Função de plotagem do Matplotlib
    'total_bill',      # Mapeado para o eixo X de cada faceta
    'tip'              # Mapeado para o eixo Y de cada faceta
)

# Adiciona a legenda para tornar a variável 'sex' interpretável
facet.add_legend()

plt.show()