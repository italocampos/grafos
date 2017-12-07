#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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


#-------------------------------------------------------
#adicionados depois

from copy import deepcopy
from grafo import Grafo

def insertionSort(G):
    
    Grafo = deepcopy(G)
    
    arestas = Grafo.getObjectAresta()
	
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