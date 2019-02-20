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


exit()

class Humano():

    def __init__(self, nome, idade, cor, peso):
        self.nome = nome
        self.idade = idade
        self.cor = cor
        self.peso = peso

    def envelhecer(self):
        self.idade += 1

class Homem(Humano):

    def __init__(self, nome, idade, cor, peso, veiculo):
        # Chama o construtor da classe de quem herdou
        #super(Homem, self).__init__(nome, idade, cor)
        super().__init__(nome, idade, cor, peso)
        self.veiculo = veiculo

    def envelhecer(self):
        self.idade += 2
        
class Mulher(Humano):

    def engravidar(self):
        self.peso += 200

paramahansa = Homem('Paramahansa Yogananda', 45, 'Negro', 85, 'Fan 125cc')
coen = Mulher('Monja Coen', 50, 'Branca', 50)
print(coen.peso)
coen.engravidar()
print(coen.peso)
exit()

for i in range(0, 10):
    print(coen.nome, coen.idade)
    coen.envelhecer()

for i in range(0, 10):
    print(paramahansa.nome, paramahansa.idade)
    paramahansa.envelhecer()
