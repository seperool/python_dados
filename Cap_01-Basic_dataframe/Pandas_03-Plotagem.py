# --- SCRIPT: OBTENDO SUBCONJUNTOS DE DADOS EM DATAFRAMES PANDAS ---

import pandas as pd # Importa a biblioteca pandas.
import matplotlib.pyplot as plt # Importa a biblioteca matplotlib para gráficos.

#------------------------------------------------------------------------------

# --- Carregamento e Inspeção Inicial ---

# Carrega o arquivo 'gapminder.tsv' em um DataFrame, usando tabulação como separador.
df = pd.read_csv(r'C:\Users\Sergio\github\python_dados\Data\Cap_01\gapminder.tsv', sep='\t')

# --- Análise e Visualização ---

# Agrupa os dados por ano e calcula a média da expectativa de vida para cada ano.
global_yearly_life_expectancy = df.groupby('year')['lifeExp'].mean()

# Exibe a média da expectativa de vida por ano.
print(global_yearly_life_expectancy)

# Cria um gráfico de linha com os anos no eixo X e a expectativa de vida no eixo Y.
plt.plot(global_yearly_life_expectancy.index, global_yearly_life_expectancy.values)

# Define o rótulo do eixo X.
plt.xlabel('Year')

# Mostra o gráfico.
plt.show()