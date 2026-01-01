#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Análise Bivariada: Gráfico de Agrupamento Hexagonal (Hexbin Plot)
Este programa utiliza o método 'hexbin' do Pandas para representar a densidade 
de pontos entre duas variáveis numéricas através de hexágonos coloridos.

Tópicos: Hexbin Plot, Densidade de Dados, Visualização de Grandes Datasets.
Created on Thu Jan  1 02:06:35 2026
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
# VISUALIZAÇÃO DE DENSIDADE (Hexbin Plot)
# ===============================================
fig, ax = plt.subplots()            # Cria moldura e área de desenho
ax = tips.plot.hexbin(
    x='total_bill',                 # Eixo X: Valor da conta
    y='tip',                        # Eixo Y: Valor da gorjeta
    gridsize=10,                    # Define o tamanho dos hexágonos
    ax=ax                           # Acopla ao objeto de eixos criado
)

plt.show()                          # Exibe o gráfico final