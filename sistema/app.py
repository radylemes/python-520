#!/usr/bin/python3
from pymongo import MongoClient
import re
import os


while True:
	try:
		os.system('clear')
		client = MongoClient()
		db = client.python

		messagem_inicial = '''
#################################
#                               #
#    Sistema de Terminal 0.1    #
#                               #
#################################

1] Buscar pelo nome
2] Cadastrar
3] Atualizar
4] Deletar
5] Listar Usuarios
6] Sair
		'''
		print(messagem_inicial)
		opcao = int(input('Selecione uma opção: '))

		if opcao <=6  and opcao != 0:
			if opcao == 1:
				nome = input('Digite o nome: ')
				nome = re.compile(nome, re.IGNORECASE)
				check = db.usuarios.find({'nome': nome}).count()
				if check == 0:
					print('Nome não localizado!!!!')
					input('Digite enter para continuar')
				else:
					for i in db.usuarios.find({'nome': nome}):
						print('{0:.<26} {1:.<30} {2: ^3}'.format(i['nome'], i['email'], i['idade']))
					input('Digite enter para continuar')

			if opcao == 2:
				nome = input('Digite o nome do usuario: ')
				email = input('Digite o email: ')
				idade = int(input('Digite a idade: '))
				senha =  input('Digite a senha: ')
				id_banco = db.usuarios.find({},{"_id" : 1}).sort([("_id", -1)]).limit(1)
				for i in id_banco:
					id_banco = (i['_id']) + 1
				db.usuarios.insert({'_id' : id_banco, 'nome' : nome, 'email' : email, 'idade' : idade, 'senha' : senha })
				print('Usuario cadastrado com sucesso!!!')
				input('Digite enter para continuar')

			if opcao == 3:
				nome = input('Digite o nome do usuario para atualizar cadastro: ')
				nome = re.compile(nome, re.IGNORECASE)
				for i in db.usuarios.find({'nome': nome}):
						id_banco = (i['_id'])
						nome = input('Digite o nome do usuario: ')
						email = input('Digite o email: ')
						idade = int(input('Digite a idade: '))
						senha =  input('Digite a senha: ')
						db.usuarios.update({'_id' : id_banco},{'_id' : id_banco, 'nome' : nome, 'email' : email, 'idade' : idade, 'senha' : senha })
				print('Atualizado com sucesso!!')

			if opcao == 4:
				for i in db.usuarios.find():
					print(i['nome'])
				nome = input('Digite o nome do usuario para exclusão: ')
				nome = re.compile(nome, re.IGNORECASE)
				for i in db.usuarios.find({'nome': nome}):
					id_banco = (i['_id'])
					db.usuarios.remove({'_id' : id_banco})
				print('Usuario removido com sucesso!!!')
				input('Digite enter para continuar')
			
			if opcao == 5:
				for i in db.usuarios.find():
					print('{0:.<26} {1:.<30} {2: ^3}'.format(i['nome'], i['email'], i['idade']))
				input('Digite enter para continuar')	

			if opcao == 6:
				print('Até logo!!!!')
				exit()
		else:
			print('Opção invalida!!!')
			input('Digite enter para continuar')

	except Exception as e:
		print(e)
		print('Erro encontrado saindo!!!!')
		break




		
























exit()

while True:
    try:
        input('Digite um nome qualquer: ')
    except:
        print('\nSaindo...')
        break



exit()
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

