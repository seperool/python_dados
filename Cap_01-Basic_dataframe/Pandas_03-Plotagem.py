# --- SCRIPT: OBTENDO SUBCONJUNTOS DE DADOS EM DATAFRAMES PANDAS ---

import pandas as pd # Importa a biblioteca pandas, atribuindo-lhe o alias 'pd'.
import matplotlib.pyplot as plt # Importa a biblioteca matplotlib para visualização de dados.

#------------------------------------------------------------------------------

# --- Carregamento e Inspeção Inicial ---

# Carrega o arquivo 'gapminder.tsv' em um DataFrame, usando tabulação como separador.
# df = pd.read_csv('../Data/Cap_01/gapminder.tsv', sep='\t')
df = pd.read_csv(r'C:\Users\Sergio\github\python_dados\Data\Cap_01\gapminder.tsv', sep='\t')

global_yearly_life_expectancy = df.groupby('year')['lifeExp'].mean()
print(global_yearly_life_expectancy)

plt.plot(global_yearly_life_expectancy.index, global_yearly_life_expectancy.values)
plt.xlabel('Year')
plt.show()