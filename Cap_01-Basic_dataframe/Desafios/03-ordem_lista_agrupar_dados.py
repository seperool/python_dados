import pandas as pd # Importa a biblioteca pandas, atribuindo-lhe o alias 'pd'.

#------------------------------------------------------------------------------
# --- Carregamento e Inspeção Inicial ---
# Carrega o arquivo 'gapminder.tsv' em um DataFrame, usando tabulação como separador.
# df = pd.read_csv('../Data/Cap_01/gapminder.tsv', sep='\t')
# Carrega o arquivo 'gapminder.tsv' em um DataFrame, usando tabulação como separador.
# O caminho do arquivo é absoluto, apontando para o local onde o arquivo está armazenado.
# O caminho pode ser ajustado conforme necessário para o ambiente de trabalho.
df = pd.read_csv(r'C:\Users\Sergio\github\python_dados\Data\Cap_01\gapminder.tsv', sep='\t')

print("--- Informações do DataFrame ---")
print("Tamanho do DataFrame (linhas, colunas):")
print(df.shape)
print("\nInformações do Dataframe:")
print(df.info())
print("\nPrimeiras 5 linhas do DataFrame (df.head())")
print(df.head())

print("\n--- Ordem da lista de agrupamentos ---")

# Agrupa o DataFrame por 'continent' e 'year', contando o número de países em cada grupo.
group_1 = df.groupby(['continent', 'year'])\
    [['lifeExp','gdpPercap']]\
    .mean()
print("\n--- Exibindo o DataFrame agrupado (group_1.head()) ---")
print(group_1.head(50))  # Exibe as primeiras linhas do DataFrame agrupado.

# Ordena o DataFrame agrupado por 'year' e 'continent'.
group_2 = df.groupby(['year', 'continent'])\
    [['lifeExp','gdpPercap']]\
    .mean()
print("\n--- Exibindo o DataFrame agrupado e ordenado (group_2.head()) ---")
print(group_2.head(50))  # Exibe as primeiras linhas do DataFrame agrupado e ordenado.