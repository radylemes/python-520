#!/usr/bin/python3

def up(letras):
    return letras.upper()

letras = ['a','Z', 'b', 'c', 'l', 'A']
ordenados = sorted(letras, key=up)

for i in ordenados:
    print(i)


