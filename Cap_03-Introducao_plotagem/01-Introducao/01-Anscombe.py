#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 17:43:50 2025

@author: sergio
"""

# O conjunto de dados Anscombe pode ser encontrado na biblioteca seaborn
import seaborn as sns
import pandas as pd

anscombe = sns.load_dataset("anscombe")
print(anscombe)

# Para ver o famoso efeito Anscombe:
print("\n--- Estatísticas Descritivas Agrupadas por Dataset (Revelação do Anscombe) ---\n")
print(anscombe.groupby('dataset').describe())
