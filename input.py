#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wes Nov 15 14:44:32 2017

@author: Fernando Junior, Italo Ramon
"""

from grafo import Grafo

def bananasplit(string):
	banana = []
	palavra = ''
	for c in string:
		if not c.isalnum() and c not in ['-', '.']:
			#if c == ' ' or palavra != '':
			if c in [' ', '\n', '\t'] or palavra != '':
				if palavra != '':
					banana.append(palavra)
					palavra = ''
			#if c != ' ':
			if c not in [' ', '\n', '\t']:
				banana.append(c)
		else:
			palavra += c
	if palavra != '':
		banana.append(palavra)
	return banana

def lerGrafo(string):
	rotulo = ''
	peso = 0.0
	aresta = []
	estado = -1
	grafo = Grafo()
	for palavra in bananasplit(string):
		if palavra == 'vertices':
			estado = 0
		elif estado == 0:
			if palavra == ',':
				estado = 1
			elif palavra == '(':
				estado = 2
			else:
				rotulo += palavra
		elif estado == 1:
			grafo.addVertice(rotulo, peso)
			rotulo = ''
			peso = 0.0
			estado = 0
			if palavra != ',':
				rotulo += palavra
		elif estado == 2:
			if palavra == ')':
				estado = 1
			else:
				peso = float(palavra)
		if palavra == 'arestas':
			break
	return grafo





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