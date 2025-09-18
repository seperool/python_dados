#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 24 16:17:53 2025

@author: sergio
"""

import pandas as pd
import numpy as np

# Series

## O que acontecerá se você usar outros contêineres Python como `list`, `tuple`,
## `dict` ou ate mesmo o `ndarray` da biblioteca `numpy`?

print("#----------------list----------------#")
s = pd.Series(['Wes McKinney', 'Creator of Pandas'])
print(s)

print("#----------------tuple----------------#")
s = pd.Series(('Wes McKinney', 'Creator of Pandas'))
print(s)

print("#----------------dict----------------#")
dict_dados = {'a':100,'b': 200, 'c':300}
s = pd.Series(dict_dados)
print(s)

print("#----------------ndarray----------------#")
numpy_dados = np.array([5,6,7])
s = pd.Series(numpy_dados)
print(s)
