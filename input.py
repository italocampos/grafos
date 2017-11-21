#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wes Nov 15 14:44:32 2017

@author: Fernando Junior, Italo Ramon
"""

from grafo import Grafo
from copy import copy

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

def readVertices(string, grafo):
	rotulo = ''
	peso = 0.0
	estado = -1

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

def readArestas(string, grafo):
	nome = ''
	rotulo = ''
	peso = 1.0
	aresta = ['', '']
	estado = -1

	for palavra in bananasplit(string):
		if palavra == 'arestas':
			estado = 0
		elif estado == 0:
			if palavra == ':':
				aresta[0] = nome; nome = ''; estado = 1
			else:
				nome += palavra
		elif estado == 1:
			if palavra == ',':
				aresta[1] = nome
				estado = 2
			elif palavra == ';':
				aresta[1] = nome
				estado = 7
			elif palavra == '(':
				aresta[1] = nome
				estado = 3
			elif palavra == '"':
				aresta[1] = nome
				estado = 5
			else:
				nome += palavra
		elif estado == 2:
			grafo.addAresta(copy(aresta), peso, rotulo)
			rotulo = ''; peso = 1.0; estado = 1; nome = ''
			if palavra != ',':
				nome = palavra
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
			grafo.addAresta(copy(aresta), peso, rotulo)
			rotulo = ''; peso = 1.0; estado = 0; nome = palavra; aresta = ['', '']
	else:
		grafo.addAresta(copy(aresta), peso, rotulo)
	
	return grafo

def readGrafo(nome_arquivo):
	grafo = Grafo(True)

	# ler o arquivo de entrada
	arquivo = open(nome_arquivo)
	string = arquivo.read()
	arquivo.close()

	# ler os vértices e arestas
	grafo = readVertices(string, grafo)
	grafo = readArestas(string, grafo)

	return grafo
