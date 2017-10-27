#!/usr/bin/env python3

def separaLista(self, linha):
	temp = linha.split()
	listapronta = []
	for item in temp:
		if item != '->':
			if item[-1] == ',':
				listapronta.append(item[:-1])
			else:
				listapronta.append(item)
	return listapronta

def addFromFile(self, namefile):
	arquivo = open(namefile, 'r')
	for linha in arquivo:
		self.lista.append(self.separaLista(linha))
	arquivo.close()