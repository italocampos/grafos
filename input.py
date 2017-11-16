#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wes Nov 15 14:44:32 2017

@author: Fernando Junior, Italo Ramon
"""

from tabela import Tabela

def bananasplit(string):
	banana = []
	palavra = ''
	for c in string:
		if not c.isalnum():
			if c == ' ' or palavra != '':
				if palavra != '':
					banana.append(palavra)
					palavra = ''
			if c != ' ':
				banana.append(c)
		else:
			palavra += c
	if palavra != '':
		banana.append(palavra)
	return banana

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