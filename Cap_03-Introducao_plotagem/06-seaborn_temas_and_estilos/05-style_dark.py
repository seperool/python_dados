#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Estilização Seaborn: Tema Dark e Violin Plot
Este programa aplica o estilo 'dark', que utiliza um fundo cinza sem linhas de 
grade, focando no contraste entre os elementos do gráfico e o fundo.

Tópicos: Seaborn set_style, Dark Style, Contraste Visual.
Created on Thu Jan  1 02:27:15 2026
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

sns.set_style('dark')               # Define fundo cinza sólido sem grade
fig, ax = plt.subplots()            # Inicializa a figura e os eixos
ax = sns.violinplot(
    x='time',                       # Variável categórica no eixo X
    y='total_bill',                 # Variável numérica no eixo Y
    hue='sex',                      # Separação por cor (Gênero)
    data=tips,                      # Fonte dos dados
    split=True                      # Divide o violino lateralmente
)

plt.show()                          # Exibe o gráfico com estilo dark aplicado