#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Análise Univariada: Histograma para Distribuição de Frequências
Este programa utiliza o método integrado do Pandas (baseado em Matplotlib) 
para gerar um histograma, permitindo visualizar a densidade e a dispersão 
da variável total_bill, identificando a concentração de valores.

Tópicos: Matplotlib subplots, Histograma Pandas, Distribuição de Dados.
Created on Wed Dec 31 02:17:07 2025
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
print("--- Visão Geral do DataFrame (Colunas e Primeiras Linhas) ---") # Imprime um cabeçalho
print(tips.columns) # Exibe o nome de todas as colunas
print(tips.head()) # Exibe as 5 primeiras linhas do DataFrame
print("-" * 30) # Imprime um separador

print("\n--- Estatísticas Descritivas (describe) ---") # Imprime um cabeçalho
print(tips.describe()) # Gera estatísticas resumidas das colunas numéricas
print("-" * 30) # Imprime um separador

print("\n--- Tipos de Dados e Saúde do DF (info) ---") # Imprime um cabeçalho
print(tips.info()) # Mostra tipos de dados, contagem de nulos e uso de memória
print("-" * 30) # Imprime um separador

# ===============================================
# VISUALIZAÇÃO UNIVARIADA (Histograma)
# ===============================================
fig, ax = plt.subplots()           # Cria a moldura (figure) e o eixo (axes)
ax = tips['total_bill'].plot.hist()# Plota a frequência da coluna especificada

plt.show()                         # Renderiza o gráfico na tela