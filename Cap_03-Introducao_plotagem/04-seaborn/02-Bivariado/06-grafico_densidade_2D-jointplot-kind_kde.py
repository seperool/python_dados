#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Python para Análise Exploratória de Dados (EDA) e Visualização
usando Pandas, Matplotlib e Seaborn.

Created on Wed Dec 3 15:27:37 2025
@author: sergio

O foco é a criação de um **Gráfico de Estimativa de Densidade Kernel Bivariada e Marginal (Joint KDE Plot)**
utilizando a função sns.jointplot e o parâmetro kind="kde".

Função do jointplot (kind="kde"):
O **jointplot** no modo 'kde' produz uma figura com três componentes visuais:
1.  Um gráfico principal (central) que visualiza a relação bivariada usando **contornos de densidade 2D**. A cor e o nível do contorno indicam a frequência/densidade conjunta das observações.
2.  Dois gráficos marginais (acima e à direita) que mostram a distribuição univariada como **curvas de densidade kernel (KDE)** para cada variável ('x' e 'y') separadamente.
Este método é ideal para visualizar a distribuição conjunta e as distribuições marginais de dados contínuos de maneira suave.
"""

# ===============================================
# IMPORTAÇÃO DE BIBLIOTECAS
# ===============================================
import pandas as pd                                  # Alias 'pd' para manipulação e análise de dados (DataFrames)
import matplotlib.pyplot as plt                      # Alias 'plt' para plotagem de gráficos e ajustes de baixo nível
import seaborn as sns                                # Alias 'sns' para visualização estatística de alto nível

# ===============================================
# CARREGAMENTO DE DADOS
# ===============================================
# Carrega o conjunto de dados 'tips' de exemplo do Seaborn
tips = sns.load_dataset("tips")                      

# ===============================================
# INSPEÇÃO DE DADOS (Análise Exploratória Inicial)
# ===============================================
print("--- Visão Geral do DataFrame (Colunas e Primeiras Linhas) ---") # Imprime um cabeçalho
print(tips.columns)                                  # Exibe o nome de todas as colunas disponíveis
print(tips.head())                                   # Exibe as 5 primeiras linhas do DataFrame
print("-" * 30)                                      # Imprime um separador

print("\n--- Estatísticas Descritivas (describe) ---") # Imprime um cabeçalho
print(tips.describe())                               # Gera estatísticas resumidas das colunas numéricas
print("-" * 30)                                      # Imprime um separador

print("\n--- Tipos de Dados e Saúde do DF (info) ---") # Imprime um cabeçalho
print(tips.info())                                   # Mostra tipos de dados, contagem de nulos e uso de memória
print("-" * 30)                                      # Imprime um separador

# ===============================================
# VISUALIZAÇÃO DE DADOS (Joint KDE Plot)
# ===============================================

# Cria o Gráfico de Junção (Joint Plot) com KDE
kde_joint = sns.jointplot( 
  x='total_bill',          # Mapeia a coluna 'total_bill' para o Eixo X
  y='tip',                 # Mapeia a coluna 'tip' para o Eixo Y
  data=tips,               # Especifica o DataFrame
  kind='kde',              # Define o tipo de plotagem como Estimativa de Densidade Kernel (KDE)
  fill=True                # O plot central será de contorno de densidade e os plots marginais serão curvas de densidade
)

# Acessa e define os rótulos dos eixos da área principal (opcional, pois jointplot já usa os nomes das colunas)
kde_joint.set_axis_labels(xlabel='Total Bill Value', ylabel='Tip Value')

# Adiciona um título geral à figura, acessando o objeto Matplotlib Figure (fig)
kde_joint.fig.suptitle('Joint KDE Plot: Total Bill vs Tip Density', y=1.03)

# Exibe o gráfico gerado
plt.show()