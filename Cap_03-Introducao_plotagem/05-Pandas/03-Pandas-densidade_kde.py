#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Análise de Densidade Kernel (KDE): Suavização de Distribuição
Este programa utiliza o método 'kde' do Pandas para gerar uma Estimativa de 
Densidade Kernel da variável 'tip', permitindo visualizar a probabilidade 
contínua da distribuição e identificar picos de frequência (modas).

Tópicos: KDE Plot, Estimativa de Densidade Kernel, Visualização Contínua.
Created on Wed Dec 31 02:34:11 2025
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
# VISUALIZAÇÃO DE DENSIDADE (Kernel Density Estimate)
# ===============================================
fig, ax = plt.subplots()           # Inicializa a figura e os eixos
ax = tips['tip'].plot.kde()        # Gera a curva de densidade de probabilidade

plt.show()                         # Renderiza o gráfico suavizado