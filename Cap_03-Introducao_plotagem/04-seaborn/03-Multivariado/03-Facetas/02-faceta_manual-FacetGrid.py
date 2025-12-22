#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Análise Multivariada com Seaborn: Facetas e Distribuições
Este programa utiliza a classe FacetGrid para decompor um conjunto de dados 
em múltiplos subplots (facetas), permitindo a comparação visual de 
variáveis contínuas segmentadas por categorias.

Tópicos: Facetagem por colunas, Mapeamento de funções (map), Seaborn Tips.
Criado em: Mon Dec 22 10:32:37 2025
@author: sergio
"""

# ===============================================
# IMPORTAÇÃO DE BIBLIOTECAS
# ===============================================
import pandas as pd             # Manipulação e análise de dados estruturados
import numpy as np              # Computação científica e operações vetoriais
import matplotlib.pyplot as plt    # Interface de plotagem de baixo nível para ajustes finos
import seaborn as sns           # Biblioteca de visualização estatística de alto nível

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
# 1. Inicializa a estrutura da grade (FacetGrid)
# O parâmetro 'col' define qual variável categórica criará as facetas laterais
facet = sns.FacetGrid(
    tips, 
    col='time'                  # Separa o gráfico por 'Lunch' (Almoço) e 'Dinner' (Jantar)
)

# 2. Mapeamento de funções para os subgráficos
# O método 'map' aplica a função escolhida em cada faceta individualmente
facet.map(
    sns.histplot,               # Usamos histplot (sucessor moderno do distplot)
    'total_bill',               # Variável analisada no eixo X
    kde=True                    # Estimativa de Densidade de Kernel (curva de suavização)
)

# Adicionando um título superior para o conjunto de facetas
plt.subplots_adjust(top=0.85)
facet.fig.suptitle('Distribuição do Valor Total por Período (Almoço vs Jantar)')

plt.show()