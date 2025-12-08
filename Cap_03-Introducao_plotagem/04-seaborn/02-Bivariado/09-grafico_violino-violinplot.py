#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Python para Análise Exploratória de Dados (EDA) e Visualização 📊
usando Pandas, Matplotlib e Seaborn.

Created on Sun Dec 7 20:50:49 2025
@author: sergio

O foco é a criação de um **Violin Plot (Gráfico de Violino)** para visualizar a
distribuição completa da variável numérica ('total_bill') agrupada pela
variável categórica ('time').

Função do violinplot (sns.violinplot):
O **sns.violinplot** combina características de um boxplot com um gráfico de
estimativa de densidade de kernel (KDE).
1. **Formato "Violino"**: A largura do "violino" em qualquer ponto representa a
   **densidade de observações** (frequência) naquele valor.
2. **Caixa/Marcadores Internos**: Geralmente, há marcadores internos (como barras)
   indicando a mediana e/ou quartis, semelhantes ao boxplot.
3. **Distribuição Completa**: Oferece uma visão mais detalhada da forma da distribuição
   dos dados (por exemplo, se é bimodal), o que o boxplot não faz.
"""

# ===============================================
# IMPORTAÇÃO DE BIBLIOTECAS
# ===============================================
import pandas as pd # Alias 'pd' para manipulação e análise de dados (DataFrames)
import numpy as np # Alias 'np' para operações numéricas (mantido, embora não usado no violinplot)
import matplotlib.pyplot as plt # Alias 'plt' para plotagem de gráficos e ajustes de baixo nível
import seaborn as sns # Alias 'sns' para visualização estatística de alto nível

# ===============================================
# CARREGAMENTO DE DADOS
# ===============================================
# Carrega o conjunto de dados 'tips' de exemplo (gorjetas) do Seaborn
tips = sns.load_dataset("tips")

# ===============================================
# INSPEÇÃO DE DADOS (Análise Exploratória Inicial)
# ===============================================
print("--- Visão Geral do DataFrame (Colunas e Primeiras Linhas) ---") # Imprime um cabeçalho para seção
print(tips.columns) # Exibe o nome de todas as colunas
print(tips.head()) # Exibe as 5 primeiras linhas para inspeção rápida
print("-" * 30) # Imprime um separador

print("\n--- Estatísticas Descritivas (describe) ---") # Imprime um cabeçalho para seção
print(tips.describe()) # Gera estatísticas resumidas das colunas numéricas
print("-" * 30) # Imprime um separador

print("\n--- Tipos de Dados e Saúde do DF (info) ---") # Imprime um cabeçalho para seção
print(tips.info()) # Mostra tipos de dados, contagem de valores não-nulos e uso de memória
print("-" * 30) # Imprime um separador

# ===============================================
# VISUALIZAÇÃO DE DADOS (Violin Plot)
# ===============================================

# Cria a figura (violin) e o eixo (ax) do Matplotlib
violin, ax = plt.subplots()

# Cria o Gráfico de Violino usando Seaborn
ax = sns.violinplot(
  x='time', # Variável categórica para o Eixo X (grupos: Dinner, Lunch)
  y='total_bill', # Variável numérica para o Eixo Y (distribuição de densidade)
  data=tips, # Especifica o DataFrame
  ax=ax, # Usa o objeto Axes criado
  inner='quartile' # Define o estilo interno (mostra Q1, Mediana e Q3)
)

# Define o título do gráfico
ax.set_title("Violin Plot do Total da Conta por Período do Dia", fontsize=14)

# Define os rótulos dos Eixos
ax.set_xlabel('Período do Dia (Time of day)', fontsize=12)
ax.set_ylabel('Total da Conta (Total Bill)', fontsize=12)

# Exibe o gráfico gerado
plt.show() # Necessário para renderizar o gráfico