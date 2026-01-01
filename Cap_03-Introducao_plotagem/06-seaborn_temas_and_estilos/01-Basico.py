#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Estilização e Gráficos de Densidade: Seaborn set_style e Violin Plot
Este programa demonstra como configurar a estética global dos gráficos com 
'set_style' e utiliza o 'violinplot' para comparar distribuições.

Tópicos: Seaborn Styles, Violin Plot, Distribuição por Categoria.
Created on Thu Jan  1 02:16:02 2026
@author: sergio
"""

# ===============================================
# IMPORTAÇÃO DE BIBLIOTECAS
# ===============================================
import pandas as pd                 # Manipulação e análise de dados
import matplotlib.pyplot as plt    # Interface de plotagem de baixo nível
import seaborn as sns               # Visualização estatística de alto nível

# ===============================================
# CARREGAMENTO DE DADOS
# ===============================================
tips = sns.load_dataset("tips")     # Carrega dataset de exemplo (Gorjetas)

# ===============================================
# INSPEÇÃO DE DADOS (Análise Exploratória Inicial)
# ===============================================
print("--- Visão Geral do DataFrame ---")
print(tips.columns)                 # Exibe o rótulo de todas as colunas
print(tips.head())                  # Exibe as 5 primeiras linhas
print("-" * 30)                     

print("\n--- Estatísticas Descritivas ---") 
print(tips.describe())              # Resumo estatístico (média, quartis, etc)
print("-" * 30)                     

print("\n--- Tipos de Dados e Saúde do DF ---") 
print(tips.info())                  # Estrutura técnica e valores não nulos
print("-" * 30)                     

# ===============================================
# VISUALIZAÇÃO DE DISTRIBUIÇÃO (Violin Plot)
# ===============================================

fig, ax = plt.subplots()            # Inicializa a figura e os eixos
ax = sns.violinplot(
    x='time',                       # Eixo X: Categoria temporal (Almoço/Jantar)
    y='total_bill',                 # Eixo Y: Valor numérico da conta
    hue='sex',                      # Diferenciação por cor (Gênero)
    data=tips,                      # Fonte dos dados
    split=True                      # Combina as metades do violino para comparação
)

plt.show()                          # Renderiza o gráfico estilizado