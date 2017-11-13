#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 22:40:32 2017

@author: Fernando Junior, Italo Ramon
"""

from vertice import Vertice

class Grafo():
	vertices = []
	arestas = []

	def addVertice(self, vertice, peso = 0):
		if(type(vertice) == list):
			for v in vertice:
				self.vertices.append(Vertice(v))
		else:
			self.vertices.append(Vertice(vertice, peso))

	def addAresta(self, aresta):
		if(type(aresta) == list) and (len(aresta) == 2):
			if(aresta[0] in self.vertices) and (aresta[1] in self.vertices):
				self.arestas.append(aresta)
			else:
				print("Aresta não pertence ao grafo.")
		else:
			print("Aresta inválida.")

	def print(self):
		print("Vertices: ", self.vertices)
		print("Arestas: ", self.arestas)
	
	def printAll(self):
		print("Vertices: ")
		for v in self.vertices:
			v.printAll()
		print("\nArestas: ", self.arestas)

	def numColumns(self, linha):
		return len(self.lista[linha]);

	def getLine(self, linha):
		if linha >= 0 and linha < self.numLines():
			return self.lista[linha]
		else:
			print("out of range")

	def getAdjacentes(self, no):
		return self.lista[self.elementIndex(no)][1:]

	def removeLine(self, linha):
		del self.lista[linha]

	def printTable(self):
		for i in self.lista:
			print (i)

	def elementIndex(self, item):
		a = 0
		for i in self.lista:
			if str(item) == i[0]:
				return a
			a += 1
		return False

	def elementIndex(self, item):
		a = 0
		for i in self.lista:
			if item == i[0]:
				return a
			a += 1
		#return False
		print("out of range")

	def getItem(self, linha, coluna):
		return self.lista[linha][coluna]