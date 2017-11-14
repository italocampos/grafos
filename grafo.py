#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 22:40:32 2017

@author: Fernando Junior, Italo Ramon
"""

from vertice import Vertice
from aresta import Aresta

class Grafo():
	vertices = []
	arestas = []
	direcionado = False

	def __init__(self, direcionado = False):
		self.direcionado = direcionado

	def addVertice(self, vertice, peso = 0):
		if(type(vertice) == list):
			for v in vertice:
				if not self.hasVertice(v):
					self.vertices.append(Vertice(v))
				else:
					print('O vértice', v, 'já existe.')
		elif not self.hasVertice(Vertice(vertice)):
			self.vertices.append(Vertice(vertice, peso))

	def __addAresta__(self, aresta, peso = 1, rotulo = ''):
		if self.hasVertice(aresta[0]) and self.hasVertice(aresta[1]):
			if not self.hasAresta(aresta):
				self.arestas.append(Aresta(aresta, peso, rotulo))
				if not self.isDirecionado():
					self.arestas.append(Aresta(aresta[::-1], peso, rotulo))
			else:
				print('A aresta', aresta, 'já existe.')
		else:
			print('A aresta ', aresta, ' não pertence ao grafo.')

	def addAresta(self, aresta, peso = 1, rotulo = ''):
		if(type(aresta) == list):
			if len(aresta) == 2 and type(aresta) != list:
				self.__addAresta__(aresta, peso, rotulo)
			else:
				for a in aresta:
					if (len(a) == 2):
						self.__addAresta__(a)
		else:
			print('Aresta inválida.')

	def isDirecionado(self):
		return self.direcionado

	def hasVertice(self, vertice):
		novo = Vertice(vertice)
		for v in self.vertices:
			if v.getRotulo() == novo.getRotulo():
				return True
		return False

	def hasAresta(self, aresta):
		nova = Aresta(aresta)
		for a in self.arestas:
			if a.getVertices() == nova.getVertices():
				return True
		return False

	def getAdjacentes(self, vertice):
		temp = []
		for t in self.arestas:
			if vertice == t.getVertices()[0] and t.getVertices()[0] not in temp:
				temp.append(t.getVertices()[1])
		return temp

	def getVertices(self):
		vertices = []
		for v in self.vertices:
			vertices.append(v.getRotulo())
		return vertices

	def getArestas(self):
		arestas = []
		for a in self.arestas:
			temp = a.getVertices()
			temp.append(a.getPeso())
			arestas.append(temp)
		return arestas

	def print(self):
		print("Vertices: ", end = '')
		for v in self.vertices:
			v.print()
			print(", ", end = '')
		print("\nArestas: ", end ='')
		for a in self.arestas:
			a.print()
			print(", ", end = '')
		print()
	
	def printAll(self):
		print("Vertices: ")
		for v in self.vertices:
			v.printAll()
		print("\nArestas: ")
		for a in self.arestas:
			a.printAll()
