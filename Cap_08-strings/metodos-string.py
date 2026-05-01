#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 20:21:13 2026

@author: sergio

ESTUDO DE MÉTODOS DE STRING EM PYTHON
-------------------------------------
Este script faz parte do meu material de estudo sobre manipulação 
de strings, explorando funções nativas de formatação, busca e validação.
"""

# --- CAPITALIZE ---
# Deixa a primeira letra da frase em maiúscula.
print('black Knight'.capitalize()) 

# --- COUNT ---
# Conta quantas vezes um caractere ou sub-string aparece.
print("It's just a flesh wound!".count('u'))

# --- STARTSWITH ---
# Verifica se a string começa com o termo especificado.
print('Halt! Who goes there?'.startswith('Halt'))

# --- ENDSWITH ---
# Verifica se a string termina com o termo especificado.
print('coconut'.endswith('nut'))

# --- FIND ---
# Retorna o índice da primeira ocorrência do termo (ou -1 se não achar).
print("It's just a flesh wound!".find('u'))

# --- INDEX ---
# Similar ao find, mas gera um erro (ValueError) se não encontrar o termo.
# print("It's just a flesh wound!".index('scratch'))

# --- ISALPHA ---
# Verifica se a string contém apenas letras (espaços retornam False).
print('old woman'.isalpha())

# --- ISDECIMAL ---
# Verifica se todos os caracteres na string são números decimais.
print('37'.isdecimal())

# --- ISALNUM ---
# Verifica se é alfanumérico (letras e números, sem símbolos ou espaços).
print("I'm 37".isalnum())

# --- LOWER ---
# Converte todos os caracteres para minúsculo.
print('Black Knight'.lower())

# --- UPPER ---
# Converte todos os caracteres para maiúsculo.
print('Black Knight'.upper())

# --- REPLACE ---
# Substitui um trecho de texto por outro.
print('flesh wound!'.replace('flesh wound', 'scratch'))

# --- STRIP ---
# Remove espaços em branco inúteis no início e no fim da string.
print(" I'm not dead. ".strip())

# --- SPLIT ---
# Divide a string em uma lista, usando um separador (espaço é o padrão).
print('NI! NI! NI!'.split(sep=' '))

# --- PARTITION ---
# Divide a string em uma tupla de 3 elementos: antes, o separador e depois.
print('3,4'.partition(','))

# --- CENTER ---
# Centraliza a string preenchendo as laterais com espaços até atingir a largura.
print('nine'.center(10))

# --- ZFILL ---
# Preenche a string com zeros à esquerda até completar a largura definida.
print('9'.zfill(5))