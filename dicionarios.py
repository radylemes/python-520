usuario = {'nome' : 'Belphegor', 'idade' : 65000, 'username' : 'bel'}

del usuario['username']

for k in usuario:
      print(usuario[k])

print(usuario.keys())
print(usuario.values())

usuario['email'] = 'bel@zebu.com'

print(usuario)

for k, v in usuario.items():
    print('{0}=> {1}'.format(k, v))
