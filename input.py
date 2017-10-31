#!/usr/bin/env python3

from tabela import Tabela

def separaLista(linha):
	temp = linha.split()
	listapronta = []
	for item in temp:
		if item != '->':
			if item[-1] == ',':
				listapronta.append(int(item[:-1]))
			else:
				listapronta.append(int(item))
	return listapronta

def addFromFile(namefile):
	tab = Tabela()
	arquivo = open(namefile, 'r')
	for linha in arquivo:
		tab.addLine(separaLista(linha))
	arquivo.close()
	return tab