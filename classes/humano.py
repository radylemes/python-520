# Criar uma clasee humano
# Que receba nome, idade e cor
# Criar um humano chamado Paramahansa Yoganda com 45 anos e negro
# Criar um humano chamado Monja Coen com 50 anos e branca

class Humano():
	
	def __init__(self, nome='', idade=0, cor=''):
		self.nome = nome
		self.idade = idade 
		self.cor = cor

	def envelhercer(self):
		self.idade += 1

	def __str__(self):
		return 'Você printou o nome do humano {0}'.format(self.nome)

class Homem(Humano):
	
	def __init__(self, nome, idade, cor, veiculo):
#		super(Homem, self).__init__(nome, idade, cor) # chama o construtor da classe de quem herdou
		super().__init__(nome, idade, cor)
		self.veiculo = veiculo		

	def envelhercer(self):
		self.idade +=2		

humano1 = Homem(nome='Paramahansa Yoganda', idade=45, cor='Negro', veiculo='Fan 125')
humano2 = Humano(nome='Monja Coen', idade=50, cor='Branca')

for i in range (0, 10):
	print(humano1.nome, humano1.idade, humano1.cor, humano1.veiculo)
	humano1.envelhercer()

for i in range (0, 10):
	print(humano2.nome, humano2.idade, humano2.cor)
	humano2.envelhercer()
