#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 18:25:59 2025

@author: sergio
"""

import pandas as pd
import numpy as np

# Cria um DataFrame de exemplo.
df = pd.DataFrame(np.arange(1, 10).reshape(3, 3), columns=list('abc'))
print("DataFrame de exemplo:\n")
print(df)

print("\n--- DataFrame e um escalar ---")
# Broadcasting: O valor escalar (10) é aplicado a cada elemento do DataFrame.
df_somado = df + 10
print(df_somado)

print("\n--- DataFrame e Series ---")
# Cria uma Series com índices que correspondem às colunas do DataFrame.
s = pd.Series([100, 200, 300], index=['a', 'b', 'c'])

# Broadcasting: A Series é alinhada pelas colunas do DataFrame (índices 'a', 'b', 'c').
# A operação é realizada coluna por coluna.
df_multiplicado = df * s
print(df_multiplicado)

print("\n--- DataFrame e DataFrame ---")
# Cria dois DataFrames com colunas que se sobrepõem parcialmente.
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
print("\ndf1:\n")
print(df1)

df2 = pd.DataFrame({'A': [10, 20], 'C': [30, 40]})
print("\ndf2:\n")
print(df2)

# Broadcasting: Os DataFrames são alinhados tanto pelo índice quanto pelas colunas.
# Onde não há alinhamento ('B' e 'C'), o pandas insere NaN.
df_soma = df1 + df2
print(df_soma)