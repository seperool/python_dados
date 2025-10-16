#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 15 04:22:26 2025

@author: sergio
"""

# ======================== 1. IMPORTAÇÃO DE BIBLIOTECAS ========================
import pandas as pd           # Importa pandas para manipulação de dados (DataFrames)
import seaborn as sns         # Importa seaborn para visualização estatística de dados
import matplotlib.pyplot as plt # Importa pyplot do matplotlib para plotagem de gráficos

# ======================== 2. CARREGAMENTO E ANÁLISE INICIAL DOS DADOS ========================
anscombe = sns.load_dataset('anscombe') # Carrega o conjunto de dados 'anscombe' (Quarteto de Anscombe)

# Agrupa por 'dataset' e imprime estatísticas descritivas para cada um (I, II, III, IV)
print(anscombe.groupby('dataset').describe())

# ======================== 3. FILTRAGEM E VISUALIZAÇÃO DE UM SUBSET ========================
dataset_1 = anscombe[anscombe['dataset'] == 'I'] # Filtra e armazena apenas os dados do 'dataset' I

plt.plot(dataset_1['x'],dataset_1['y']) # Cria um gráfico de linha (x vs y) para o 'dataset' I
plt.show()
# (Nota: Para exibir o gráfico, seria necessário adicionar plt.show())