#!/usr/bin/python3

#arquivo = open('zen.txt').read().upper()
arquivo = open('zen.txt')
#print(type(arquivo))
#print(arquivo.readlines())
for linha in arquivo:
    if '-' not in linha[0]:
#   linha = linha.strip()
#   if linha != '-':
        print(linha, end='')
#

