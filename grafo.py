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

	def addVertice(self, vertice, peso = 0):
		if(type(vertice) == list):
			for v in vertice:
				if not self.hasVertice(v):
					self.vertices.append(Vertice(v))
				else:
					print("O vértice", v, "já existe no grafo")
		else:
			self.vertices.append(Vertice(vertice, peso))

	def addAresta(self, aresta):
		if(type(aresta) == list) and (len(aresta) == 2):
			if self.hasVertice(aresta[0]) and self.hasVertice(aresta[1]):
				if not self.hasAresta(aresta):
					self.arestas.append(Aresta(aresta))
				else:
					print("A aresta", aresta, "já existe no grafo")
			else:
				print("Aresta não pertence ao grafo.")
		else:
			print("Aresta inválida.")

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

	def print(self):
		print("Vertices: ")
		for v in self.vertices:
			v.print()
		print("\nArestas: ")
		for a in self.arestas:
			a.print()
	
	def printAll(self):
		print("Vertices: ")
		for v in self.vertices:
			v.printAll()
		print("\nArestas: ")
		for a in self.arestas:
			a.printAll()
    
	def getAdjacentes(self, vertice):
		temp = []
		for t in self.arestas:
			if vertice == t.getVertices()[0] and t.getVertices()[0] not in temp:
				temp.append(t.getVertices()[1])
			elif vertice == t.getVertices()[1] and t.getVertices()[1] not in temp:
				temp.append(t.getVertices()[0])
		return temp