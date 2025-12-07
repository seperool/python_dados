#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Python para Análise Exploratória de Dados (EDA) e Visualização
usando Pandas, Matplotlib e Seaborn.

Created on Sun Dec 7 20:42:00 2025
@author: sergio

O foco é a criação de um **Boxplot (Gráfico de Caixa)** para visualizar a distribuição
da variável numérica ('total_bill') agrupada pela variável categórica ('time').

Função do boxplot (sns.boxplot):
O **sns.boxplot** exibe a distribuição de dados numéricos através de seus quartis.
Ele mostra:
1. **Mediana (linha central)**: O valor que separa a metade superior da inferior dos dados.
2. **Caixa (IQR)**: Abrange o Intervalo Interquartil (IQR), do 1º Quartil (Q1) ao 3º Quartil (Q3), representando 50% dos dados.
3. **Fios (Whiskers)**: Estendem-se da caixa para indicar a dispersão dos dados.
4. **Outliers (pontos)**: Pontos de dados que caem além dos limites dos fios.
"""

# ===============================================
# IMPORTAÇÃO DE BIBLIOTECAS
# ===============================================
import pandas as pd                                # Alias 'pd' para manipulação e análise de dados (DataFrames)
import numpy as np                                 # Alias 'np' para operações numéricas (mantido, embora não usado no boxplot)
import matplotlib.pyplot as plt                    # Alias 'plt' para plotagem de gráficos e ajustes de baixo nível
import seaborn as sns                              # Alias 'sns' para visualização estatística de alto nível

# ===============================================
# CARREGAMENTO DE DADOS
# ===============================================
# Carrega o conjunto de dados 'tips' de exemplo (gorjetas) do Seaborn
tips = sns.load_dataset("tips")                    

# ===============================================
# INSPEÇÃO DE DADOS (Análise Exploratória Inicial)
# ===============================================
print("--- Visão Geral do DataFrame (Colunas e Primeiras Linhas) ---") # Imprime um cabeçalho para seção
print(tips.columns)                                # Exibe o nome de todas as colunas
print(tips.head())                                 # Exibe as 5 primeiras linhas para inspeção rápida
print("-" * 30)                                    # Imprime um separador

print("\n--- Estatísticas Descritivas (describe) ---") # Imprime um cabeçalho para seção
print(tips.describe())                             # Gera estatísticas resumidas das colunas numéricas
print("-" * 30)                                    # Imprime um separador

print("\n--- Tipos de Dados e Saúde do DF (info) ---") # Imprime um cabeçalho para seção
print(tips.info())                                 # Mostra tipos de dados, contagem de valores não-nulos e uso de memória
print("-" * 30)                                    # Imprime um separador

# ===============================================
# VISUALIZAÇÃO DE DADOS (Boxplot)
# ===============================================

# Cria a figura (box) e o eixo (ax) do Matplotlib
box, ax = plt.subplots()

# Cria o Gráfico de Caixa (Boxplot) usando Seaborn
ax = sns.boxplot(
  x='time', # Variável categórica para o Eixo X (grupos: Dinner, Lunch)
  y='total_bill', # Variável numérica para o Eixo Y (distribuição)
  data=tips # Especifica o DataFrame
)

# Define o título do gráfico
ax.set_title('Boxplot do Total da Conta por Período do Dia')

# Define os rótulos dos Eixos
ax.set_xlabel('Período do Dia (Time of day)')
ax.set_ylabel('Total da Conta (Total Bill)')

# Exibe o gráfico gerado
plt.show() # Necessário para renderizar o gráfico