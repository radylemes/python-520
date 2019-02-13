#!/usr/bin/python3
#Exibir o nome do primeiro filho de quem tem filho

usuarios = [{"nome": "Hector", "idade" : 27, "email" : "hector.silva@4linux.com.br"},
            {"nome": "Leonel", "idade" : 50,"email" : "leoneldesouza@gmail.com", 'filhos' : ['Ana', 'João', 'Antônio']},
            {"nome": "Hugo", "idade" : 36, "email" : "hleosousa@bol.com.br"},
            {"nome": "Guilherme Serafim", "idade" : 27, "email" : "guisilvaserafim@gmail.com"},
            {"nome": "Joel", "idade" : 28, "email" : "oliveira.shiai@yahoo.com.br"},
            {"nome": "Ayron", "idade" : 28, "email" : "ayron_pedro@hotmail.com", 'filhos' : ['Belzebu', 'Belphegor', 'Baphomet']},
            {"nome": "Lucas", "idade" : 25, "email" : "lucas.salles@4linux.com.br"},
            {"nome": "Roger", "idade" : 23, "email" : "rogeralexandre95@gmail.com"},
            {"nome": "Victor Lapetina", "idade" : 23, "email" : "victor.lrs95@gmail.com"},
            {"nome": "Cicero", "idade" : 52, "email" : "jose.cicero@gmail.com", 'filhos' : ['Nicko', 'Xiphorimphola']},
            {"nome": "Daniel", "idade" : 37, "email" : "danylemis@yahoo.com.br"},
            {"nome": "Fabiano", "idade" : 36, "email" : "fabianobat@gmail.com"},
            {"nome": "Flavio", "idade" : 43, "email" : "flaviogpacheco@hotmail.com", 'filhos' : ['Pedro', 'Paulo', 'Peterson']},
            {"nome": "Guilherme Ayres", "idade" : 23, "email" : "gui.ayres@hotmail.com"}]

for u in usuarios:
    if 'filhos' in u:
        print(u['filhos'][0])
exit()

# Escrever com print o meu email

usuarios = [{"nome": "Hector", "idade" : 27, "email" : "hector.silva@4linux.com.br"},
{"nome": "Leonel", "idade" : 50,"email" : "leoneldesouza@gmail.com"},
{"nome": "Hugo", "idade" : 36, "email" : "hleosousa@bol.com.br"},
{"nome": "Guilherme Serafim", "idade" : 27, "email" : "guisilvaserafim@gmail.com"},
{"nome": "Joel", "idade" : 28, "email" : "oliveira.shiai@yahoo.com.br"},
{"nome": "Ayron", "idade" : 28, "email" : "ayron_pedro@hotmail.com"},
{"nome": "Lucas", "idade" : 25, "email" : "lucas.salles@4linux.com.br"},
{"nome": "Roger", "idade" : 23, "email" : "rogeralexandre95@gmail.com"},
{"nome": "Victor Lapetina", "idade" : 23, "email" : "victor.lrs95@gmail.com"},
{"nome": "Cicero", "idade" : 52, "email" : "jose.cicero@gmail.com"},
{"nome": "Daniel", "idade" : 37, "email" : "danylemes@yahoo.com.br"},
{"nome": "Fabiano", "idade" : 36, "email" : "fabianobat@gmail.com"},
{"nome": "Flavio", "idade" : 43, "email" : "flaviogpacheco@hotmail.com"},
{"nome": "Guilherme Ayres", "idade" : 23, "email" : "gui.ayres@hotmail.com"}]


print(usuarios[0]['email'])

for u in usuarios:
#   print(u['email'])
    print('NOME: {0:.>20} Email: {1:.>30}'.format(u['nome'], u['email']))  

exit()
usuarios = [[1,2,'daniel'],[3,4,5,'andre'],[5,6,6,'Teste']]

for u in usuarios:
    for i in u:
        if type(i) == str:
            print(i.upper())

# Exibir o último número de cada lista

for usuario in usuarios:
    print(usuario[-1])


exit()
letras = ['a','b','c','e','f']
v1, *v2 = letras
print (v2)


