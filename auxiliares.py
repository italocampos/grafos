#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Módulo com as funções auxiliares aos algoritmos de operações nos grafos

from copy import deepcopy
from grafo import Grafo

def isExplorada(exploradas, aresta):
	if [aresta[0],aresta[1]] in exploradas: return True
	if [aresta[1],aresta[0]] in exploradas: return True
	return False


def insertionSort(G):
	Grafo = deepcopy(G)

	arestas = Grafo.getObjectArestas()

	for i in range(1,len(arestas)):
		x = arestas[i]
		j = i-1
		while j>=0 and x.getPeso() < arestas[j].getPeso():
			Grafo.arestas[j+1] = Grafo.arestas[j]
			j=j-1
		Grafo.arestas[j+1] = x

	return Grafo


def removeItens(total, praRemover):
	temp = []

	for element in total:
		temp.append(element)

	for element in temp:
		if element in praRemover:
			del total[total.index(element)]

	return total


def minFranja(Franjas):
	if Franjas != []:
		min = Franjas[0]
		for t in Franjas:
			if t[1] < min[1]:
				min = t
		return min
	else:
		print("Não existem franjas")


def extrairMin(lista, Q):
	for i in lista:
		if i[0] in Q:
			u = i;
			break

	q = []

	for element in lista:
		if element[0] in Q:
			q.append(element[0])
		if element[1] < u[1] and element[0] in Q:
			u = element

	del q[q.index(u[0])]

	return u, q


# lista contém elementos no formato [vertice, distancia, origem]
# lista2 contém somente elementos adjacentes de um dado vertice
# Deve ser retornado os correspondentes da lista na lista2
# Retorna uma lista de vértices adjacentes aos vértices 'lista'
# no formato [vertice, distancia, origem]
def selecionaAdj(lista, lista2):
	retorno = []
	
	for i in lista2:
		for j in lista:
			if i == j[0]:
				retorno.append(j)
				continue
	return retorno;
	

def pesoAresta(lista, aresta):
	for element in lista:
		if aresta == element[0]:
			return element[1]


''' Seja x uma máscara tal que x = [[[A1, B1], p1], [[A2, B2], p2], ..., [[An, Bn], pn]], 
onde Ai, Bi são componentes de uma aresta e pi são os seus respectivos pesos. '''

# Retorna os vertices de uma subárvore da forma x
def vertices(subarvore):
	vertices = []
	for aresta in subarvore:
		if aresta[0][0] not in vertices:
			vertices.append(aresta[0][0])
		if aresta[0][1] not in vertices:
			vertices.append(aresta[0][1])
	return vertices


''' 'subarvore' e 'alcancadas' são listas na forma x. 'subarvore' representa uma subarvore
qualquer e 'alcancadas' representa as arestas de subárvores que já foram alcancadas.'''
def isAlcancada(subarvore, alcancadas):
	# Captura os vértices da subárvore
	v = vertices(subarvore)
	# Verifica se algum dos vértices da subárvore foi alcancado
	for aresta in alcancadas:
		if aresta[0][1] in v:
			return True
	return False


def unificar(floresta):
	flora = deepcopy(floresta)
	nova_floresta = []
	while flora != []:
		nova_subarvore = flora[0]
		flora.remove(flora[0])
		# Verifica se existe interseção entre a nova subárvore as outras da floresta e as unifica
		for subarvore in flora:
			ver = vertices(nova_subarvore)
			for v in ver:
				if v in vertices(subarvore):
					nova_subarvore += subarvore
					flora.remove(subarvore)
					break
		nova_floresta.append(nova_subarvore)
	return nova_floresta



def setFlorestaInicial(vertices):
	floresta = []
	for v in vertices:
		floresta.append([[[v, v], 0]])
	return floresta
