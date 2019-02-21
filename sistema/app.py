#!/usr/bin/python3

from modulos.mysql import dados
from modulos.mysql import cb

nome = input('Digite o nome do usuario: ')
email = input('Digite o email: ')
sql_email = "SELECT * FROM usuarios WHERE email = '{0}'".format(email)
resultado = dados.execute(sql_email)
if resultado == 1:
	print('Email ja cadastrado!!!')
	exit()
sexo = input('Digite o sexo: ')
if 'Masculino' in sexo.title():
		sexo = 0
elif 'Feminino' in sexo.title():
	sexo = 1
else:
	print('Opção invalida', sexo)
	exit()
gravar = "INSERT INTO usuarios (nome, email, sexo) VALUES (%s, %s,%s)"
dados.execute(gravar, (nome, email, sexo))
cb.cnn.commit()

sql = "SELECT * FROM usuarios "
dados.execute(sql)

for i in dados:
	print(i)

