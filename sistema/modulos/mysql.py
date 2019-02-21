#!/usr/bin/python3

from MySQLdb import connect
from MySQLdb.cursors import DictCursor

class Consulta_Banco():

	def __init__(self):
		self.cnn = connect(host='127.0.0.1', user='python', passwd='4linux123', db='python', cursorclass=DictCursor)
		
cb = Consulta_Banco()
dados = cb.cnn.cursor()

