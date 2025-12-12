#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Python para Análise Exploratória de Dados (EDA) e Visualização
usando Pandas, Matplotlib e Seaborn.

Created on Fri Dec 12 15:23:10 2025
@author: sergio

Este script carrega o conjunto de dados 'tips' e realiza uma inspeção inicial.
O foco principal é a **Visualização de Dados** através da criação de um
**Violin Plot (Gráfico de Violino)** customizado usando o Seaborn.

O Gráfico de Violino é útil para visualizar a distribuição de uma variável
quantitativa (total_bill) através de categorias (time, sex), combinando
elementos de box plot e KDE (Estimativa de Densidade de Kernel).
"""

# ===============================================
# IMPORTAÇÃO DE BIBLIOTECAS
# ===============================================
import pandas as pd # Alias 'pd' para manipulação e análise de dados (DataFrames)
import numpy as np # Alias 'np' para operações numéricas (mantido, embora não usado diretamente)
import matplotlib.pyplot as plt # Alias 'plt' para plotagem de gráficos e ajustes de baixo nível
import seaborn as sns # Alias 'sns' para visualização estatística de alto nível

# ===============================================
# CARREGAMENTO DE DADOS
# ===============================================
# Carrega o conjunto de dados 'tips' de exemplo (gorjetas) diretamente do Seaborn
tips = sns.load_dataset("tips")

# ===============================================
# INSPEÇÃO DE DADOS (Análise Exploratória Inicial)
# ===============================================
print("--- Visão Geral do DataFrame (Colunas e Primeiras Linhas) ---") # Imprime um cabeçalho para seção
print(tips.columns) # Exibe o nome de todas as colunas do DataFrame
print(tips.head()) # Exibe as 5 primeiras linhas para inspeção rápida da estrutura
print("-" * 30) # Imprime um separador (30 hífens)

print("\n--- Estatísticas Descritivas (describe) ---") # Imprime um cabeçalho para seção
print(tips.describe()) # Gera estatísticas resumidas das colunas numéricas (contagem, média, desvio padrão, quartis)
print("-" * 30) # Imprime um separador (30 hífens)

print("\n--- Tipos de Dados e Saúde do DF (info) ---") # Imprime um cabeçalho para seção
# Mostra tipos de dados, contagem de valores não-nulos e uso de memória
tips.info()
print("-" * 30) # Imprime um separador (30 hífens)

# ===============================================
# VISUALIZAÇÃO DE DADOS (Violin Plot)
# ===============================================

violin, ax = plt.subplots() # Cria uma figura e um conjunto de eixos para o gráfico
ax = sns.violinplot(
  x='time', # Variável categórica para o eixo X (Eixos principais: Dia/Noite)
  y='total_bill', # Variável quantitativa para o eixo Y (Distribuição do valor da conta)
  hue='sex', # Variável categórica adicional para diferenciar (Dividir por Gênero)
  data=tips, # Define o DataFrame a ser usado
  split=True # Dividir os violinos para as categorias 'hue' dentro de cada 'x'
) # Gera o gráfico de violino

# Exibe o gráfico gerado.
plt.show() # Renderiza a visualização final do Violin Plot