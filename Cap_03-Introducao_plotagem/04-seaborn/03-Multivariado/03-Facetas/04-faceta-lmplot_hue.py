#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Visualização Multivariada Otimizada: Facetas com lmplot
Este programa utiliza a função lmplot do Seaborn para realizar uma análise 
multivariada comparativa, mapeando variáveis de dispersão (x, y), 
cor (hue) e facetas de colunas (col) simultaneamente.

Tópicos: Seaborn lmplot, Facetas de Coluna, Variáveis Categóricas e Numéricas.
Created on Mon Dec 22 10:45:58 2025
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
# VISUALIZAÇÃO MULTIVARIADA (Facetas com lmplot)
# ===============================================
# O lmplot gerencia automaticamente a criação de facetas e legendas.
fig = sns.lmplot(
    x='total_bill',    # Eixo X: Variável numérica contínua (valor da conta)
    y='tip',           # Eixo Y: Variável numérica contínua (valor da gorjeta)
    data=tips,         # Fonte dos dados (DataFrame)
    fit_reg=False,     # Define se deve exibir a reta de regressão linear
    hue='sex',         # Dimensão de cor: separa por gênero (terceira variável)
    col='day'          # Dimensão de faceta: separa em colunas por dia (quarta variável)
)

plt.show()