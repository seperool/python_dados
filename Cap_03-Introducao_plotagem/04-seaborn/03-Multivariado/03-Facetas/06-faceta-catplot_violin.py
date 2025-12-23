#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Análise Multivariada com Catplot: Facetas e Distribuições de Violino
Este programa utiliza a função de nível de figura 'catplot' para criar uma 
matriz complexa que analisa a distribuição do valor da conta (total_bill) 
através de cinco dimensões: dias, gênero (hue), fumantes (row) e horário (col).

Tópicos: Seaborn catplot, Gráficos de Violino, Matriz de Facetas.
Created on Mon Dec 22 10:54:33 2025
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
# VISUALIZAÇÃO MULTIVARIADA (Matriz de Facetas com catplot)
# ===============================================
# O catplot é ideal para variáveis categóricas em eixos ou facetas.
facet = sns.catplot(
    x='day',           # Eixo X: Variável categórica ordinal (Dias da semana)
    y='total_bill',    # Eixo Y: Variável numérica contínua (Valor da conta)
    hue='sex',         # Cor: Diferenciação por gênero dentro de cada violino
    data=tips,         # DataFrame de origem
    row='smoker',      # Facetas de Linha: Separa fumantes de não fumantes
    col='time',        # Facetas de Coluna: Separa horários (Lunch/Dinner)
    kind='violin',     # Tipo de Visualização: Gráfico de violino (densidade + boxplot)
    split=True,        # Opcional sugerido: combina os sexos em um único violino dividido
    height=2.5,        # Altura de cada faceta
    aspect=1           # Relação largura/altura
)

plt.show()