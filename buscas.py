#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from copy import deepcopy
from grafo import Grafo
infinito = 1000000000000000000000000000000000000000000000000000000000

def isExplorado(exploradas, aresta):
    if [aresta[0],aresta[1]] in exploradas: return True
    if [aresta[1],aresta[0]] in exploradas: return True
    return False

def buscaProfundidade(grafo, no, marcados, exploradas, retorno):
    marcados.append(no)
    for item in grafo.getAdjacentes(no):
        if item not in marcados:
            exploradas.append([no,item])
            marcados.append(no)
            marcados, exploradas, retorno = buscaProfundidade(grafo, item, marcados, exploradas, retorno)
        else:
            if not isExplorado(exploradas, [no,item]):
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
            elif not isExplorado(exploradas, [v,no]):
                exploradas.append([v,no])
                retorno.append([v,no])
    return marcados, removeItens(exploradas,retorno), retorno

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
	
#lista contém elementos no formato [nome, distancia, origem]
#lista2 contém somente dos elementos adjacentes
#Deve ser retornado os correspondentes da lista na lista2
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
			#a variável u é retornada no formato [nome, distancia, origem]

			
			
			u, Q = extrairMin(vertices, Q)
			#a variável v é retornada no formato [nome, distancia, origem]
			v = selecionaAdj(vertices, grafo.getAdjacentes(u[0]))
					
			for element in v:
				if element[1] > u[1] + pesoAresta(arestas, [u[0],element[0]]):
					element[1] = u[1] + pesoAresta(arestas, [u[0],element[0]])
					element[2] = u[0]
					if element[0] not in Q: 
						Q.append(element[0])      
		return vertices
	else:
		print("não foi possivel executar a funcao, pois a aresta dada nao está no grafo!")