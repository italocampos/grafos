#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from copy import deepcopy
from grafo import Grafo
from auxiliares import *
infinito = 1000000000000000000000000000000000000000000000000000000000

def buscaProfundidade(grafo, no, marcados, exploradas, retorno):
	marcados.append(no)
	for item in grafo.getAdjacentes(no):
		if item not in marcados:
			exploradas.append([no,item])
			marcados.append(no)
			marcados, exploradas, retorno = buscaProfundidade(grafo, item, marcados, exploradas, retorno)
		else:
			if not isExplorada(exploradas, [no,item]):
				exploradas.append([no,item])
				retorno.append([no,item])
	return marcados, removeItens(exploradas,retorno), retorno


def buscaLargura(grafo, vertice_inicial):
	marcados = []
	fila = []
	exploradas = []
	retorno = []
	# marcando vertice_inicial
	marcados.append(vertice_inicial)
	# coloca na fila de nohs sendo explorados
	fila.append(vertice_inicial)
	while fila != []:
		v = fila[0]
		del fila[0]
		adjacentes = grafo.getAdjacentes(v) #adjacentes do noh vigente
		for no in adjacentes:
			if no not in marcados:
				exploradas.append([v,no])
				fila.append(no)
				marcados.append(no)
			elif not isExplorada(exploradas, [v,no]):
				exploradas.append([v,no])
				retorno.append([v,no])
	return marcados, removeItens(exploradas,retorno), retorno

	
def prim(g, i):
	grafo = g
	T = [i]
	V = removeItens(grafo.getVertices(), T)
	Arv_Min = []
	
	while V != []:
		K = minFranja(grafo.getFranja(T))
		T += [K[0][1]]
		V = removeItens(V,T)
		Arv_Min.append(K)
		
	return Arv_Min


def kruskal(grafo):
	H = insertionSort(grafo)

	T = Grafo(False)
	T.addVertice(H.getVertices())
	T.addAresta(H.arestas[0].getVertices(), H.arestas[0].getPeso())

	i = 2

	while i < len(H.getArestas()) :
		K = deepcopy(T)
		K.addAresta(H.arestas[i].getVertices())
		_,_,retorno = buscaProfundidade(K,H.arestas[i].getVertices()[0],[],[],[])
		if len(retorno) == 0:
			T.addAresta(H.arestas[i].getVertices(), H.arestas[i].getPeso())
		i += 2

	return T


def dijkstra (grafo, inicial):
	if grafo.hasVertice(inicial):
		
		vertices = []
		arestas = grafo.getArestas()
		
		#criando uma lista dos vertices do grafo, contendo nome do vértice, distancia para chegar nele e a origem
		for i in grafo.vertices:
			if i.getRotulo() == inicial:
				vertices.append([i.getRotulo(), 0, inicial])
			else:
				vertices.append([i.getRotulo(), infinito, ''])

		Q = grafo.getVertices()

		while Q != []:
			
			#funcao que extrai o vertice com menor distância da lista de vértices 
			#e elimina esse elemento da lista
			#a variável u é retornada no formato [vertice, distancia, origem]
			
			u, Q = extrairMin(vertices, Q)
			#a variável v é retornada no formato [vertice, distancia, origem]
			v = selecionaAdj(vertices, grafo.getAdjacentes(u[0]))
					
			for element in v:
				if element[1] > u[1] + pesoAresta(arestas, [u[0],element[0]]):
					element[1] = u[1] + pesoAresta(arestas, [u[0],element[0]])
					element[2] = u[0]
					if element[0] not in Q: 
						Q.append(element[0])      
		return vertices
	else:
		print("Não foi possivel executar a função, pois a aresta dada não está no grafo!")


def boruvka(grafo):
	floresta = grafo.getVertices()
	subarvore = []
 
