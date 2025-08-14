# Importa a biblioteca pandas, essencial para manipulação de dados
import pandas as pd

# Carrega o arquivo 'gapminder.tsv' em um DataFrame
# O 'sep' é usado para indicar que o separador de colunas é uma tabulação (\t)
df = pd.read_csv(r'C:\Users\Sergio\github\python_dados\Data\Cap_01\gapminder.tsv', sep='\t')

# Exibe informações completas sobre o DataFrame (df.info())
print("--- Informações Completas do DataFrame (df.info()) ---")
print(df.info())

# Exibe as primeiras 5 linhas do DataFrame para uma visualização rápida
print("\n--- Primeiras 5 linhas do DataFrame (df.head()) ---")
print(df.head())

# --- Fatiamento das colunas ---

# 1º pergunta: Seleciona as colunas da 0 (inclusive) até a 6 (exclusiva), com passo 1 (padrão)
# Isso resulta nas colunas de índice 0, 1, 2, 3, 4 e 5
print("\n--- 1º pergunta ---")
subcolumn = df.iloc[:, 0:6:]
print(subcolumn.head())

# 2º pergunta: Seleciona as colunas da 0 (inclusive) até o final, pulando de 2 em 2
# Isso seleciona as colunas de índice 0, 2, 4, 6, etc.
print("\n--- 2º pergunta ---")
subcolumn = df.iloc[:, 0::2]
print(subcolumn.head())

# 3º pergunta: Seleciona as colunas da 0 (inclusive) até a 6 (exclusiva), pulando de 2 em 2
# Isso seleciona as colunas de índice 0, 2 e 4
print("\n--- 3º pergunta ---")
subcolumn = df.iloc[:, :6:2]
print(subcolumn.head())

# 4º pergunta: Seleciona todas as colunas do início ao fim, pulando de 2 em 2
# Isso seleciona as colunas de índice 0, 2, 4, 6, etc. (igual à 2ª pergunta, mas com sintaxe diferente)
print("\n--- 4º pergunta ---")
subcolumn = df.iloc[:, ::2]
print(subcolumn.head())

# 5º pergunta: Seleciona todas as colunas do início ao fim, com passo 1 (padrão)
# Isso cria uma cópia exata do DataFrame original com todas as colunas
print("\n--- 5º pergunta ---")
subcolumn = df.iloc[:, ::]
print(subcolumn.head())