#!/usr/bin/python3

from MySQLdb import connect
from MySQLdb.cursors import DictCursor


db = connect(host='127.0.0.1', user='python', passwd='4linux123', db='python', cursorclass=DictCursor)

cursor = db.cursor()
cursor.execute('SELECT * FROM usuarios')

for linha in cursor:
	print(linha)