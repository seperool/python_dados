#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Estudo de Dados Multivariados: Facetas e Codificação por Cor (Hue)
Este programa utiliza a biblioteca Seaborn para explorar a relação entre 
duas variáveis numéricas (total_bill e tip) segmentadas por variáveis 
categóricas (day e sex) através de grades de subplots.

Tópicos: Seaborn FacetGrid, Mapeamento de Dispersão, Análise por Hue.
Created on Mon Dec 22 10:41:03 2025
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
# O dataset 'tips' é um padrão para estudos multivariados (valor da conta, gorjeta, dia, tempo)
tips = sns.load_dataset("tips") 

# ===============================================
# INSPEÇÃO DE DADOS (Análise Exploratória Inicial)
# ===============================================
print("--- Visão Geral do DataFrame ---")
print(tips.head())              # Visualização das primeiras entradas para entender as variáveis
print("-" * 30)

print("\n--- Estatísticas Descritivas ---")
print(tips.describe())          # Resumo estatístico (média, desvio padrão, quartis)
print("-" * 30)

# ===============================================
# VISUALIZAÇÃO MULTIVARIADA (Facetas com FacetGrid)
# ===============================================
# Faceta multivariada: 'col' cria subplots por dia e 'hue' diferencia gênero por cor
facet = sns.FacetGrid(      # Define a grade por 'day' e cores por 'sex'
  tips,
  col='day',
  hue='sex'
)

facet = facet.map(          # Mapeia o gráfico de dispersão para a grade
  plt.scatter,              # Define a função de plotagem (matplotlib)
  'total_bill',             # Variável do eixo X (Independente)
  'tip'                     # Variável do eixo Y (Dependente)
)
facet = facet.add_legend()  # Adiciona a legenda para identificar as cores do 'hue'

plt.show()