#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Python para Análise Exploratória de Dados (EDA) e Visualização
usando Pandas e Seaborn.

Created on Fri Nov  7 15:40:43 2025
@author: sergio

O foco é a criação de um Histograma Univariado utilizando sns.histplot.

Diferença entre histplot e Alternativas:
O **histplot** é a função de "nível de Axes" do Seaborn, ideal para plotar um único gráfico
e que permite integração direta com objetos Axes do Matplotlib (via 'ax=...').
É o sucessor direto e a versão mais flexível do antigo `sns.distplot` (agora obsoleto).
Ao contrário do `displot` (função de alto nível), o `histplot` não suporta o Faceting
automático (subgráficos com 'col' ou 'row'), mas oferece maior controle sobre o Axes individual.
"""

# ===============================================
# IMPORTAÇÃO DE BIBLIOTECAS
# ===============================================
import pandas as pd             # Importa pandas, essencial para a manipulação e estruturação de dados (DataFrames).
import matplotlib.pyplot as plt # Importa o módulo de plotagem do Matplotlib para funcionalidades de baixo nível e customização.
import seaborn as sns           # Importa Seaborn, uma biblioteca de alto nível para gráficos estatísticos.

# ===============================================
# CARREGAMENTO DE DADOS
# ===============================================
tips = sns.load_dataset("tips") # Carrega o conjunto de dados de exemplo 'tips' (Gorjetas) diretamente do repositório do Seaborn.

# ===============================================
# INSPEÇÃO DE DADOS (Análise Exploratória Inicial)
# ===============================================
print("--- Visão Geral do DataFrame (Colunas e Primeiras Linhas) ---") # Título para a seção.
print(tips.columns)               # Exibe os nomes das colunas disponíveis no DataFrame.
print(tips.head())                # Exibe as 5 primeiras linhas para verificar a estrutura e o formato dos dados.
print("-" * 30)                   # Separador visual.

print("\n--- Estatísticas Descritivas (describe) ---") # Título da seção.
print(tips.describe())            # Gera estatísticas resumidas (média, desvio padrão, quartis) para as colunas numéricas.
print("-" * 30)

print("\n--- Tipos de Dados e Saúde do DF (info) ---") # Título da seção.
print(tips.info())                # Fornece um resumo conciso do DataFrame, incluindo tipos de dados (dtypes) e contagem de valores não-nulos.
print("-" * 30)

# ===============================================
# CRIAÇÃO DA VISUALIZAÇÃO (HISTOGRAMA UNINVARIADO)
# ===============================================
# Criação explícita de Figure e Axes, que é a prática recomendada ao usar Matplotlib/Seaborn juntos.
# Figure (hist) é a tela; Axes (ax) é o gráfico real.
hist, ax = plt.subplots()        # Cria o objeto Figure (hist) e o objeto Axes (ax) em uma única chamada.

# Cria e plota o Histograma usando sns.histplot (o método preferido para distribuição)
ax = sns.histplot(data=tips,          # Passa o DataFrame completo como fonte de dados.
                  x='total_bill',     # Especifica a coluna a ser plotada no eixo X.
                  bins=15,            # Define que a variável será dividida em 15 intervalos.
                  kde=True,           # Adiciona a Curva de Estimativa de Densidade de Kernel (KDE) para suavizar a distribuição.
                  ax=ax)              # Garante que o gráfico seja desenhado no objeto Axes criado ('ax').

# Adiciona customizações estéticas ao plot usando o objeto 'ax'
ax.set_title("Total Bill Histogram") # Define o título principal do Axes.
ax.set_xlabel("Total Bill")      # Define o rótulo do eixo X.
ax.set_ylabel("Frequency")       # Define o rótulo do eixo Y.

# Exibe a visualização
plt.show()                       # Renderiza e exibe o gráfico configurado.