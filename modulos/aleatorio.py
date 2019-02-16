import time, random, datetime
from subprocess import run, PIPE
from sentidos.som import FREQUENCIA, doppler

print(FREQUENCIA)
doppler()

exit()
#r = subprocess.run(['free', '-h'], stdout=subprocess.PIPE)

r = run(['apt-get', 'install' , '-y', 'sl'], stdout=PIPE, stderr=PIPE)

if r.returncode !=0:
	print('Deu merda!!!!')


#print(dir(r))
#print(r.stdout.decode('utf-8'))

exit()
letras = ['A', 'B', 'C', 'D']

print(random.randint(100, 999))

time.spleep(1)

print(random.choice(letras))

print(datetime.datetime.now())

hoje = datetime.datetime.now()
print(hoje.strftime('%d/%m/%Y'))
