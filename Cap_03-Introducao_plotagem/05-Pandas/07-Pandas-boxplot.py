#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Análise Univariada e Comparativa: Gráfico de Caixa (Boxplot)
Este programa utiliza o método 'box' do Pandas para visualizar a distribuição 
estatística de variáveis numéricas, destacando a mediana, quartetos e outliers.

Tópicos: Boxplot, Dispersão, Mediana, Identificação de Outliers.
Created on Thu Jan  1 02:11:36 2026
@author: sergio
"""

# ===============================================
# IMPORTAÇÃO DE BIBLIOTECAS
# ===============================================
import pandas as pd                 # Manipulação e análise de dados
import numpy as np                  # Operações matemáticas e vetoriais
import matplotlib.pyplot as plt    # Interface base para gráficos
import seaborn as sns               # Fornece datasets e estilos

# ===============================================
# CARREGAMENTO DE DADOS
# ===============================================
tips = sns.load_dataset("tips")     # Carrega dados sobre gorjetas

# ===============================================
# INSPEÇÃO DE DADOS (Análise Exploratória Inicial)
# ===============================================
print("--- Visão Geral do DataFrame ---")
print(tips.columns)                 # Lista nomes das colunas
print(tips.head())                  # Exibe primeiras 5 linhas
print("-" * 30)                     

print("\n--- Estatísticas Descritivas ---") 
print(tips.describe())              # Resumo estatístico numérico
print("-" * 30)                     

print("\n--- Tipos de Dados e Saúde do DF ---") 
print(tips.info())                  # Resumo de tipos e nulos
print("-" * 30)                     

# ===============================================
# VISUALIZAÇÃO DE DISTRIBUIÇÃO (Boxplot)
# ===============================================

fig, ax = plt.subplots()            # Inicializa figura e eixos
ax = tips.plot.box(
    ax=ax                           # Desenha o boxplot nos eixos criados
)

plt.show()                          # Renderiza o gráfico na tela