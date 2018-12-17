# -*- coding: utf-8 -*-
import rpyc

# Conecta no servidor RPC
conn = rpyc.connect('127.0.0.1', 18861)

# Abre o arquivo com a descrição do grafo
def read_file(file_name):
	file = open(file_name)
	return file.read()

string = read_file('simple.in')

# ret possui a referência ao serviço disponibilizado com os métodos no servidor
print(conn.root.create_graph(string))

print('Input is in <string>')
print('Service reference is in <conn>')