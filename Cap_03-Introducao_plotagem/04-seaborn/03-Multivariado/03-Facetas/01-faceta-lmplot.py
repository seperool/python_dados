#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Análise de Dados Multivariados: Visualização com Facetas (Seaborn)
Este programa demonstra o uso de funções de nível de figura (lmplot) para
explorar o Quarteto de Anscombe, utilizando facetas para separar categorias 
e comparar distribuições estatísticas visualmente.

Tópicos: Seaborn, FacetGrid (col, col_wrap), Matplotlib.
Criado em: Mon Dec 22 10:20:17 2025
@author: sergio
"""

# ===============================================
# IMPORTAÇÃO DE BIBLIOTECAS
# ===============================================
import pandas as pd             # Manipulação de tabelas e estruturas de dados
import numpy as np              # Operações matemáticas e vetoriais
import matplotlib.pyplot as plt    # Ajustes finos de layout e exibição
import seaborn as sns           # Visualização estatística baseada em objetos

# ===============================================
# CARREGAMENTO DE DADOS
# ===============================================
# O dataset 'anscombe' é ideal para estudar facetas, pois contém 4 subconjuntos 
# com estatísticas idênticas, mas distribuições visuais distintas.
anscombe = sns.load_dataset('anscombe') 

# ===============================================
# INSPEÇÃO DE DADOS (Análise Exploratória Inicial)
# ===============================================
print("--- Visão Geral do DataFrame (Colunas e Primeiras Linhas) ---")
print(anscombe.columns)                      # Exibe o nome de todas as colunas do DataFrame
print(anscombe.head())                       # Exibe as 5 primeiras linhas para inspeção rápida da estrutura
print("-" * 30)

print("\n--- Estatísticas Descritivas (describe) ---")
print(anscombe.describe())                   # Gera estatísticas resumidas das colunas numéricas
print("-" * 30)

print("\n--- Tipos de Dados e Saúde do DF (info) ---")
print(anscombe.info())                       # Mostra tipos de dados, contagem de valores não-nulos e memória
print("-" * 30)


# ===============================================
# VISUALIZAÇÃO MULTIVARIADA (Facetas com lmplot)
# ===============================================
# O lmplot é um wrapper de alto nível para o FacetGrid. 
# Ele permite mapear uma variável categórica para diferentes subplots (facetas).

anscombe_plot = sns.lmplot(
    x='x',                   # Variável numérica contínua (Eixo X)
    y='y',                   # Variável numérica contínua (Eixo Y)
    data=anscombe,           # DataFrame de origem
    fit_reg=False,           # Desativa a linha de regressão linear para focar nos pontos
    
    # Parâmetros de Facetagem:
    col='dataset',           # Cria uma faceta (coluna) para cada valor único em 'dataset'
    col_wrap=2,              # Organiza a grade: quebra a linha após 2 colunas
    
    # Parâmetros Estéticos:
    height=4,                # Define a altura de cada faceta individual (em polegadas)
    aspect=1,                # Define a proporção (1 = largura igual à altura)
    scatter_kws={"s": 50, "alpha": 0.7} # Customiza o tamanho e transparência dos pontos
)

# Ajuste fino do título geral (suptitulo) para considerar as facetas
plt.subplots_adjust(top=0.9)
anscombe_plot.fig.suptitle('Análise Comparativa: Quarteto de Anscombe', fontsize=14)

plt.show()