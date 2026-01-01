#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Estilização Seaborn: Tema White e Violin Plot
Este programa aplica o estilo 'white', que remove a grade de fundo para um visual
mais limpo e minimalista, focado totalmente nos dados.

Tópicos: Seaborn set_style, White Style, Estética Minimalista.
Created on Thu Jan  1 02:24:34 2026
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
# CONFIGURAÇÃO DE ESTILO E PLOTAGEM
# ===============================================

sns.set_style('white')              # Remove a grade e define fundo branco
fig, ax = plt.subplots()            # Inicializa a figura e os eixos
ax = sns.violinplot(
    x='time',                       # Variável categórica no eixo X
    y='total_bill',                 # Variável numérica no eixo Y
    hue='sex',                      # Separação por cor (Gênero)
    data=tips,                      # Fonte dos dados
    split=True                      # Divide o violino lateralmente
)

plt.show()                          # Exibe o gráfico com estilo limpo