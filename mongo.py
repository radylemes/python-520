#!/usr/bin/python3
from pymongo import MongoClient

client = MongoClient()
db = client.python

nome = input('Digite o nome do usuario: ')
email = input('Digite o email: ')
idade = input('Digite a idade: ')

db.usuarios.insert({'_id': 6, 'nome' : nome, 'email' : email, 'idade' : idade })

exit()

for i in db.usuarios.find():
	if 'filhos' in i:
		for f in i['filhos']:
			if f['nome'] == 'Jose':
				print(f['nome'])