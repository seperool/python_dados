#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 29 04:19:19 2025

@author: sergio
"""

"""
Programa de Análise de Gorjetas (Tips Dataset).

Carrega e explora o dataset 'tips' do Seaborn. O script realiza:
1. Exploração inicial dos dados (head, shape, info, describe).
2. Transformação de dados: recodifica a coluna 'sex' para valores numéricos.
3. Criação de um gráfico de dispersão (scatter plot) para visualizar a
   relação entre 'total_bill' e 'tip', utilizando 'sex' para cor e 'size' para tamanho dos pontos.
"""

# ========================
# Importação de Bibliotecas
# ========================
import pandas as pd              # Importa a biblioteca pandas para manipulação de dados
import matplotlib.pyplot as plt  # Importa a biblioteca matplotlib para visualização estática
import seaborn as sns            # Importa a biblioteca seaborn para visualização estatística

# ====================
# Preparação dos Dados
# ====================
tips = sns.load_dataset('tips')  # Carrega o conjunto de dados de exemplo 'tips' do seaborn

# ============================
# Descrição e Exploração Inicial
# ============================
print("====================================")
print("Amostra das 5 Primeiras Linhas (tips.head()):")
print("====================================")
print(tips.head()) # Exibe as 5 primeiras linhas do DataFrame

print("\n====================================")
print("Número Total de Elementos (tips.size):")
print("====================================")
print(tips.size) # Exibe o número total de células (linhas * colunas)

print("\n====================================")
print("Dimensões do DataFrame (tips.shape - Linhas, Colunas):")
print("====================================")
print(tips.shape) # Exibe o número de linhas e colunas

print("\n====================================")
print("Nomes das Colunas (tips.columns):")
print("====================================")
print(tips.columns) # Exibe os nomes de todas as colunas

print("\n====================================")
print("Informações Detalhadas (tips.info()):")
print("====================================")
print(tips.info()) # Exibe informações como tipos de dados e valores não-nulos (Nota: tips.info() imprime diretamente e retorna None)

print("\n====================================")
print("Estatísticas Descritivas (tips.describe()):")
print("====================================")
print(tips.describe()) # Exibe estatísticas (média, desvio padrão, quartis) para colunas numéricas


# ==================================
# Transformação: Recodificação de Sexo
# ==================================
print("\n====================================")
print("Recodificando 'sex' para 'sex_color':")
print("====================================")
# Cria uma variável de cor baseada em sexo
def recode_sex(sex):             # Define a função para recodificar o sexo para valores numéricos
  if sex == 'Female':            # Se o sexo for 'Female'
    return 0                     # Retorna 0
  else:                          # Caso contrário (sexo for 'Male')
    return 1                     # Retorna 1
print("Função 'recode_sex' criada: Female=0, Male=1") # Descrição sucinta da função

tips['sex_color'] = tips['sex'].apply(recode_sex) # Aplica a função para criar a nova coluna 'sex_color'

# =======================
# Criação do Gráfico
# =======================
scatter_plot = plt.figure()      # Cria uma nova figura para o gráfico
axes1 = scatter_plot.add_subplot(1,1,1) # Adiciona um subplot (1 linha, 1 coluna, posição 1)
axes1.scatter(                   # Cria o gráfico de dispersão (scatter plot)
  x=tips['total_bill'],          # Define a coluna 'total_bill' para o eixo X
  y=tips['tip'],                 # Define a coluna 'tip' para o eixo Y

  # Define o tamanho dos pontos com base no tamanho dos grupos;
  # Multiplicamos os valores por 10 para deixar os pontos maiores
  # e enfatizar as diferenças.
  s=tips['size']*10,             # Define o tamanho dos pontos ('s') usando a coluna 'size' multiplicada por 10

  # Define a cor para o sexo.
  c=tips['sex_color'],           # Define a cor ('c') dos pontos usando a coluna 'sex_color'

  # Define o valor de alpha para que os pontos sejam mais transparentes.
  # Isso ajuda no caso de pontos que se sobrepõem.
  alpha=0.5                      # Define a transparência ('alpha') dos pontos para 0.5
)
axes1.set_title('Total Bill vs Tip Colored by Sex and Sized by Size') # Define o título do gráfico
axes1.set_xlabel('Total Bill')   # Define o rótulo do eixo X
axes1.set_ylabel('tip')          # Define o rótulo do eixo Y

# =======================
# Exibição do Gráfico
# =======================
plt.show()                       # Exibe a figura e o gráfico