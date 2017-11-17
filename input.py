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

def readVertices(string):
	rotulo = ''
	peso = 0.0
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

def readEdges(string, grafo):
	vertice = ''
	rotulo = ''
	peso = 1.0
	aresta = ['', '']
	estado = -1

	for palavra in bananasplit(string):
		if palavra == 'arestas':
			estado = 0
		elif estado == 0:
			if palavra == ':':
				aresta[0] = vertice; vertice = ''; estado = 1
			else:
				vertice += palavra
		elif estado == 1:
			if palavra == ',':
				aresta[1] = vertice
				estado = 2
			elif palavra == ';':
				aresta[1] = vertice
				estado = 7
			elif palavra == '(':
				aresta[1] = vertice
				estado = 3
			elif palavra == '"':
				aresta[1] = vertice
				estado = 5
			else:
				vertice += palavra
		elif estado == 2:
			grafo.addAresta(aresta, peso, rotulo)
			print("DEBUG: aresta = ", aresta, ", peso = ", peso, ", rotulo = ", rotulo)
			rotulo = ''; peso = 1.0; estado = 1; vertice = ''
			if palavra != ',':
				vertice = palavra
		elif estado == 3:
			if palavra == ')':
				estado = 4
			else:
				peso = float(palavra)
		elif estado == 4:
			if palavra == '"':
				estado = 5
			elif palavra == ';':
				estado = 7
			elif palavra == ',':
				estado = 2
		elif estado == 5:
			if palavra == '"':
				estado = 6
			else:
				rotulo += palavra
		elif estado == 6:
			if palavra == ';':
				estado = 7
			elif palavra == ',':
				estado = 2
		elif estado == 7:
			grafo.addAresta(aresta, peso, rotulo)
			print("DEBUG: aresta = ", aresta, ", peso = ", peso, ", rotulo = ", rotulo)
			rotulo = ''; peso = 1.0; estado = 0; vertice = palavra; aresta = ['', '']
	else:
		grafo.addAresta(aresta, peso, rotulo)
		print("DEBUG: aresta = ", aresta, ", peso = ", peso, ", rotulo = ", rotulo)
	
	return grafo

def readGraph(nome_arquivo):
	grafo = Grafo(True)

	# ler o arquivo de entrada
	arquivo = open(nome_arquivo)
	string = arquivo.read()
	arquivo.close()

	# ler os vértices
	grafo = readVertices(string)
	grafo = readEdges(string, grafo)

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
