# -*- coding: utf-8 -*-
"""
MÓDULOS_E_BIBLIOTECAS_PYTHON.py

Este arquivo serve como um catálogo centralizado para importação de bibliotecas
e módulos Python comumente utilizados em projetos de análise de dados,
machine learning e desenvolvimento geral.

O objetivo é fornecer uma visão rápida das ferramentas disponíveis,
incluindo:

- Módulos nativos e de sistema (os, sys, math, etc.).
- Bibliotecas para manipulação e computação de dados (NumPy, Pandas).
- Ferramentas de Machine Learning (TensorFlow, Keras, Scikit-learn).
- Bibliotecas para visualização de dados (Matplotlib, Seaborn, Pygal).
- Módulos de suporte para I/O, testes e formatação.

Autor: Sergio
Data de Criação: Sat Mar 30 23:07:22 2024
"""

################################################################################
#                   MÓDULOS DE SISTEMA, UTILITÁRIOS E NATIVOS                  #
################################################################################
import os                        # Interage com o sistema operacional
import sys                       # Acesso a variáveis e funções do interpretador Python
import math                      # Funções matemáticas
import statistics                # Funções estatísticas
import datetime                  # Manipulação de datas e horas
import collections               # Tipos de dados especializados (dicionários, filas, etc.)
import json                      # Leitura e escrita de arquivos JSON
import csv                       # Leitura e escrita de arquivos CSV
import xlwt                      # Escrever em formato Excel antigo (.xls)
import openpyxl                  # Ler e escrever em formato Excel moderno (.xlsx)
import odo                       # Simplifica a transferência de dados entre diversos formatos (ex: CSV para SQL, DataFrame).
import unittest                  # Framework para testes de unidade
import random                    # Geração de números pseudoaleatórios

################################################################################
#               BIBLIOTECAS DE COMPUTAÇÃO E ANÁLISE DE DADOS                   #
################################################################################
import numpy as np               # Computação numérica de alto desempenho (arrays e matrizes)
import pandas as pd              # Estrutura de dados e ferramentas para análise de dados

################################################################################
#                       BIBLIOTECAS DE MACHINE LEARNING                        #
################################################################################
import tensorflow as tf          # Aprendizado de máquina (Google)
from tensorflow import keras     # API de alto nível para redes neurais
from tensorflow.keras import layers # Camadas comuns para construção de redes neurais

import sklearn                   # Biblioteca de aprendizado de máquina (scikit-learn)

################################################################################
#                     BIBLIOTECAS DE VISUALIZAÇÃO DE DADOS                     #
################################################################################
import matplotlib.pyplot as plt # Criação de gráficos estáticos e interativos
import seaborn as sns            # Visualização estatística de dados, baseada no Matplotlib
import Pygal                     # Criação de gráficos vetoriais escaláveis (SVG)

################################################################################
#                              BIBLIOTECAS ADICIONAIS                          #
################################################################################
import kivy                      # Framework para desenvolvimento de aplicativos multi-touch
from IPython.display import Markdown # Ferramenta para renderizar texto como Markdown
from tabulate import tabulate    # Formata dados tabulares para texto