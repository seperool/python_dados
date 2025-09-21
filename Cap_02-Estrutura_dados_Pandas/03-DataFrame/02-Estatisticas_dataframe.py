#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 21 19:59:13 2025

@author: sergio
"""

import pandas as pd

df = pd.read_csv("../scientists.csv")

print(df.head(5))
print(df.columns)
print(df.info())
print(df.shape)

# Funções de estatistica