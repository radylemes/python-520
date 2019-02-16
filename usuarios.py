#!/usr/bin/python3
# git add .
# git commit -m 'Exercicio final da aula 3'
# git push origin master

# Escrever os nomes e os usuários da seguinte forma:
# hector................ ....hector.silva@4linux.com.br



lista = []
for l in open('usuarios.csv'):
    nome, idade, email = l.split(',')
    lista.append({"nome" : nome.strip(),"email" : email.strip(),"idade" : int(idade.strip())})

def hprint():
	return '{0: ^6}    {1:.<20} {2:.<34}'.format('ID','NOME','EMAIL')
	
def fprint(n, m):
	n = n.zfill(2)
	print('{2: ^6}--> {0:.<20} {1:.>34}'.format(m['nome'], m['email'], n))

print(hprint())

for i, u in enumerate(sorted(lista, key=lambda u : u["nome"]), start=1):
	fprint(str(i), u)

exit()


for u in sorted(lista, key=lambda i : i["nome"]):
    print('{0:.<20} {1:.>35}'.format(u['nome'], u['email']))

exit()
ordenados = []
for i in lista:
#    print(i['nome'])
    ordenados.append(i['nome'])
for n in sorted(ordenados):
    print(n)
