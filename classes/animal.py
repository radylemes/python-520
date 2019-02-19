#classe que define uma abstração de mamíferos


class Animal():

#	def __init__(self, peso=0, idade=0, cor='', nome='', especie=''):
#	def __init__(self, *args):
#		self.peso = args[0] if len(args) >= 1 else 0
#		self.idade = args[1] if len(args) >= 2 else 0
#		self.cor = args[2] if len(args) >= 3 else ''
#		self.nome = args[3] if len(args) >= 4 else ''
#		self.especie = args[4] if len(args) >= 5 else ''

	def __init__(self, **kwargs):
		for k in kwargs:
			self [k] = kwargs[k]

#		self.peso = kwargs['peso'] if 'peso' in kwargs else ''
#		self.idade = kwargs['idade'] if 'idade' in kwargs else ''
#		self.cor = kwargs['cor'] if 'cor' in kwargs else ''
#		self.nome = kwargs['nome'] if 'nome' in kwargs else ''
#		self.especie = kwargs['especie'] if 'especie' in kwargs else ''

	def __str__(self):
		return 'Você printou o gatinho {0}'.format(self.nome)
	
	def __setitem__(self, key, value):
		setattr(self, key, value)

gatinho = Animal(nome='Manfred', cor='Rosa')
gatinho2 = Animal(nome='Gatinha',cor='Pink')

print(gatinho)
print(gatinho2)
