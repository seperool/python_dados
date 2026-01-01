#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Estilização Seaborn: Tema Whitegrid e Violin Plot
Este programa demonstra a aplicação do estilo 'whitegrid' para melhorar a 
leitura de valores através de linhas de grade sobre um fundo branco.

Tópicos: Seaborn set_style, Whitegrid, Visualização de Distribuição.
Created on Thu Jan  1 02:20:12 2026
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

sns.set_style('whitegrid')          # Ativa fundo branco com grade cinza clara
fig, ax = plt.subplots()            # Inicializa a figura e os eixos
ax = sns.violinplot(
    x='time',                       # Variável categórica no eixo X
    y='total_bill',                 # Variável numérica no eixo Y
    hue='sex',                      # Separação por cor (Gênero)
    data=tips,                      # Fonte dos dados
    split=True                      # Divide o violino para comparar categorias
)

plt.show()                          # Exibe o gráfico com estilo aplicado