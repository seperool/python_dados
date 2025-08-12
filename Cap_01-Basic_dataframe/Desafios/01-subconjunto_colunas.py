import pandas as pd

# Carrega o arquivo 'gapminder.tsv' em um DataFrame, usando tabulação ('\t') como separador.
df = pd.read_csv(r'C:\Users\Sergio\github\python_dados\Data\Cap_01\gapminder.tsv', sep='\t')

print("--- Informações Completas do DataFrame (df.info()) ---")
# Exibe um resumo do DataFrame, incluindo o tipo de dado de cada coluna e a quantidade de valores não nulos.
print(df.info())

# Pega o último índice de coluna. O .shape[1] retorna o número total de colunas.
# Subtraímos 1 para obter o último índice (já que os índices começam em 0).
column_max = df.shape[1] - 1
print("\nnúmero total de colunas: ")
# Exibe o número total de colunas do DataFrame.
print(column_max + 1)

print("\n--- O que acontece se tentar acessar um invervalo maior que o nº colunas existente ---")
try:
    # Cria uma lista de índices que excede o número de colunas.
    # O '+3' garante que o intervalo vai além do índice da última coluna.
    num_range = list(range(0, column_max + 3))

    # Tenta selecionar as colunas usando o método .iloc.
    # A seleção falhará porque o 'num_range' contém índices que não existem no DataFrame.
    subset = df.iloc[:, num_range]
    print(subset.head())
except IndexError as e:
    # Captura e exibe o erro que ocorre quando tentamos acessar índices fora do limite.
    print(f"Erro: {e}")
else:
    # Este bloco é executado somente se nenhum erro ocorrer.
    # Na prática, ele não será executado neste caso.
    print("Nenhum erro ocorreu ao tentar acessar colunas fora do intervalo.")