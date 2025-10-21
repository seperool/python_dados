#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 02:53:08 2025

@author: sergio
"""

# ======================== 1. IMPORTAÇÃO DE BIBLIOTECAS ========================
import pandas as pd         # Importa pandas para manipulação de dados (DataFrames)
import seaborn as sns       # Importa seaborn para visualização estatística de dados
import matplotlib.pyplot as plt # Importa pyplot do matplotlib para plotagem de gráficos

# ======================== 2. CARREGAMENTO E ANÁLISE INICIAL DOS DADOS ========================
anscombe = sns.load_dataset('anscombe') # Carrega o conjunto de dados 'anscombe' (Quarteto de Anscombe)

# ----------------- SEPARAÇÃO DOS DATASETS -----------------
# Filtra e isola cada um dos quatro datasets (I, II, III e IV)
dataset_1 = anscombe[anscombe['dataset'] == 'I']
dataset_2 = anscombe[anscombe['dataset'] == 'II']
dataset_3 = anscombe[anscombe['dataset'] == 'III']
dataset_4 = anscombe[anscombe['dataset'] == 'IV']

# ======================== 3. CRIAÇÃO DA ESTRUTURA DE PLOTAGEM (FIGURE E AXES) ========================
fig = plt.figure() # Cria o objeto 'Figure' (a tela/container do gráfico)

# ----------------- CRIAÇÃO DOS SUBGRÁFICOS (EIXOS) -----------------
# a subplotegem tem 2 linhas e 2 colunas, local 1 de plotegem
axes1 = fig.add_subplot(2,2,1) # Adiciona o primeiro subgráfico (Eixos) na posição 1
# a subplotegem tem 2 linhas e 2 colunas, local 2 de plotegem
axes2 = fig.add_subplot(2,2,2) # Adiciona o segundo subgráfico (Eixos) na posição 2
# a subplotegem tem 2 linhas e 2 colunas, local 3 de plotegem
axes3 = fig.add_subplot(2,2,3) # Adiciona o terceiro subgráfico (Eixos) na posição 3
# a subplotegem tem 2 linhas e 2 colunas, local 4 de plotegem
axes4 = fig.add_subplot(2,2,4) # Adiciona o quarto subgráfico (Eixos) na posição 4

# ======================== 4. PLOTAGEM DOS DADOS EM CADA EIXO ========================
axes1.plot(dataset_1['x'], dataset_1['y'],"o") # Plota dataset 1 (x vs y) com marcadores de círculo ("o")
axes2.plot(dataset_2['x'], dataset_2['y'],"o") # Plota dataset 2 (x vs y)
axes3.plot(dataset_3['x'], dataset_3['y'],"o") # Plota dataset 3 (x vs y)
axes4.plot(dataset_4['x'], dataset_4['y'],"o") # Plota dataset 4 (x vs y)

# ======================== 5. CONFIGURAÇÃO FINAL E EXIBIÇÃO ========================
# ----------------- DEFINIÇÃO DOS TÍTULOS DOS SUBGRÁFICOS -----------------
axes1.set_title("dataset_1") # Define o título do subgráfico 1
axes2.set_title("dataset_2") # Define o título do subgráfico 2
axes3.set_title("dataset_3") # Define o título do subgráfico 3
axes4.set_title("dataset_4") # Define o título do subgráfico 4

# ----------------- TÍTULO GERAL E LAYOUT -----------------
# adiciona um título para toda figura
fig.suptitle("Anscombe Data") # Adiciona um título centralizado para a Figura inteira

# usa um layout organizado
fig.tight_layout() # Ajusta automaticamente os parâmetros do subgráfico para um layout compacto

plt.show() # Exibe a Figura com os quatro gráficos