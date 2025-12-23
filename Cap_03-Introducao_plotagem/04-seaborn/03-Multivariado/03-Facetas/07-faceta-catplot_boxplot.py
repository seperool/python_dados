#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Análise Multivariada: Matriz de Boxplots para Identificação de Quartis
Este programa utiliza o 'catplot' para decompor a variável total_bill em uma 
matriz de facetas, permitindo comparar a dispersão, medianas e a presença 
de outliers entre dias, sexos, fumantes e horários.

Tópicos: Seaborn catplot, Boxplot, Outliers, Facetagem Bidimensional.
Created on Mon Dec 22 10:57:25 2025
@author: sergio
"""

# ===============================================
# IMPORTAÇÃO DE BIBLIOTECAS
# ===============================================
import pandas as pd              # Manipulação e análise de dados estruturados
import numpy as np               # Computação científica e operações vetoriais
import matplotlib.pyplot as plt    # Interface de plotagem de baixo nível
import seaborn as sns            # Visualização estatística de alto nível

# ===============================================
# CARREGAMENTO DE DADOS
# ===============================================
tips = sns.load_dataset("tips") 

# ===============================================
# INSPEÇÃO DE DADOS (Análise Exploratória Inicial)
# ===============================================
print("--- Visão Geral do DataFrame ---")
print(tips.head())
print("-" * 30)

# ===============================================
# VISUALIZAÇÃO MULTIVARIADA (Matriz de Facetas com Boxplot)
# ===============================================
# O catplot com kind='box' facilita a comparação de estatísticas descritivas
facet = sns.catplot(
    x='day',           # Eixo X: Categorias ordinais (Dias da semana)
    y='total_bill',    # Eixo Y: Variável numérica contínua (Mediana e Quartis)
    hue='sex',         # Cor: Comparação direta de gênero dentro de cada dia
    data=tips,         # Conjunto de dados
    row='smoker',      # Facetas de Linha: Separação por hábito de fumar
    col='time',        # Facetas de Coluna: Separação por período do dia
    kind='box',        # Tipo: Diagrama de caixa (Box-and-Whisker plot)
    height=2.5,        # Dimensão vertical de cada subplot
    aspect=1           # Proporção entre largura e altura
)

plt.show()