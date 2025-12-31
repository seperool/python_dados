#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Análise Bivariada: Gráfico de Dispersão (Scatter Plot)
Este programa utiliza o método 'scatter' do Pandas para explorar a relação 
entre duas variáveis numéricas, permitindo identificar a correlação, a 
concentração de dados e possíveis valores atípicos (outliers).

Tópicos: Scatter Plot, Correlação Visual, Análise de Relacionamento.
Created on Wed Dec 31 02:37:52 2025
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
# VISUALIZAÇÃO DE RELACIONAMENTO (Scatter Plot)
# ===============================================
fig, ax = plt.subplots()           # Inicializa a figura e os eixos
ax = tips.plot.scatter(
    x='total_bill',                # Eixo X: Variável independente (Conta total)
    y='tip',                       # Eixo Y: Variável dependente (Gorjeta)
    ax=ax                          # Direciona a plotagem para o eixo criado
)

plt.show()                         # Exibe o gráfico de dispersão