#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 22:40:32 2017

@author: Fernando Junior, Italo Ramon
"""

class Tabela():
	lista = []

	def addLine(self, lista):
		self.lista.append(lista)

	def numLines(self):
		return len(self.lista);

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