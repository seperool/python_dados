#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Análise Exploratória e Histograma Comparativo de DataFrame
Este programa executa uma inspeção estrutural de um DataFrame (colunas, tipos e 
estatísticas) e utiliza o Pandas para plotar histogramas sobrepostos, permitindo 
comparar a distribuição de 'total_bill' e 'tip' com transparência.

Tópicos: Inspeção de DataFrame (info/describe), Histogramas Sobrepostos, Alpha Blending.
Created on Wed Dec 31 02:28:59 2025
@author: sergio
"""

# ===============================================
# IMPORTAÇÃO DE BIBLIOTECAS
# ===============================================
import pandas as pd                # Manipulação e análise de dados estruturados
import numpy as np                 # Computação científica e operações vetoriais
import matplotlib.pyplot as plt    # Interface de plotagem de baixo nível
import seaborn as sns              # Visualização estatística de alto nível

# ===============================================
# CARREGAMENTO DE DADOS
# ===============================================
tips = sns.load_dataset("tips")    # Carrega dataset de exemplo (Gorjetas)

# ===============================================
# INSPEÇÃO DE DADOS (Análise Exploratória Inicial)
# ===============================================
print("--- Visão Geral do DataFrame (Colunas e Primeiras Linhas) ---")
print(tips.columns)                # Exibe o rótulo de todas as colunas
print(tips.head())                 # Exibe as 5 primeiras linhas do DataFrame
print("-" * 30)                    

print("\n--- Estatísticas Descritivas (describe) ---") 
print(tips.describe())             # Resumo estatístico (média, quartis, etc)
print("-" * 30)                    

print("\n--- Tipos de Dados e Saúde do DF (info) ---") 
print(tips.info())                 # Estrutura técnica e valores não nulos
print("-" * 30)                    

# ===============================================
# VISUALIZAÇÃO COMPARATIVA (Histogramas Sobrepostos)
# ===============================================
fig, ax = plt.subplots()           # Inicializa a figura e os eixos
ax = tips[['total_bill','tip']].plot.hist(
  alpha=0.5,                       # Define opacidade para visualização de sobreposição
  bins=20,                         # Define a quantidade de faixas (bins)
  ax=ax                            # Direciona a plotagem para o eixo criado
)

plt.show()                         # Exibe o gráfico finalizado