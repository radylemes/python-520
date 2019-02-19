def checkint(valor, nome):
    if not valor.isnumeric():
        print('Campo {0} inválido'.format(nome))
        exit()
    return valor

def checklen(valor, minimo, nome):
    if len(valor) < minimo:
        print('Campo {0} menor do que {1}'.format(nome, minimo))
        exit()
    return valor
#!/usr/bin/python3

from functions import checkint

id = checkint(input('Digite o id do usuário: '), 'id')
nome = checklen(input('Digite o nome do usuário: '), 10, 'nome')
login = checklen(input('Digite o login do usuário: '), 6, 'login')
idade = checkint(input('Digite a idade do usuário: '), 'idade')
setor = checkint(input('Digite o setor do usuário: '), 'setor')