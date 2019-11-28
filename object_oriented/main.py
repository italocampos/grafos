#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from algoritmos import *
from grafo import *
from input import *

def main():

	grafoPrimBoruvkaKruskal = lerGrafo("prim_kruskal_boruvka.in")
	grafoDijkstra = lerGrafo("dijkstra.in")
	grafoBellmanFord = lerGrafo("bellmanford.in")
	grafoFloydWarshall = lerGrafo("floydwarshall.in")
	
	
	#======================================================================================================
	
	
	print("Grafo usado: ")
	grafoPrimBoruvkaKruskal.printAll()
	
	inicial = grafoPrimBoruvkaKruskal.vertices[0].getRotulo()
	
	
	print("---------------------------------------------------------")
	print("Busca em largura")
	marcados, exploradas, retorno = buscaLargura(grafoPrimBoruvkaKruskal, inicial)
	print("Resultados da busca em largura no grafo:")
	print("Noh inicial: ", inicial)
	print("Arestas exploradas: ", exploradas)
	print("Arestas de retorno: ", retorno, "\n")
	
	#------------------------------
	
	print("---------------------------------------------------------")
	print("Busca em profundidade")
	marcados, exploradas, retorno = buscaProfundidade(grafoPrimBoruvkaKruskal, inicial, [], [], [])
	print("Resultados da busca em profundidade:")
	print("Noh inicial: ", inicial)
	print("Arestas exploradas: ", exploradas)
	print("Arestas de retorno: ", retorno)
	
	
	#======================================================================================================
	
	
	print("---------------------------------------------------------")
	print("Algoritmo de Prim")
	Arv_Min = prim(grafoPrimBoruvkaKruskal, inicial)
	print("Resultados do algorimo de Prim:")
	print("Noh inicial: ", inicial)
	print("Arvore Minima: ", Arv_Min)
	
	#------------------------------
	
	print("---------------------------------------------------------")
	print("Algoritmo de Kruskal")
	Arv_Min = kruskal(grafoPrimBoruvkaKruskal)
	print("Resultados do algorimo de Kruskal:")
	print("Arvore Minima: ", Arv_Min)
	
	
	print("---------------------------------------------------------")
	print("Algoritmo de Boruvka")
	Arv_Min = boruvka(grafoPrimBoruvkaKruskal)
	print("Resultados do algorimo de Boruvka:")
	print("Arvore Minima: ", Arv_Min)
	
	#======================================================================================================
	
	print("---------------------------------------------------------")
	print("Grafo usado para o algoritmo de Dijkstra: ")
	grafoDijkstra.printAll()
	print("---------------------------------------------------------")
	inicial = grafoDijkstra.vertices[0].getRotulo()
	
	
	print("---------------------------------------------------------")
	print("Algoritmo de Dijkstra")
	retorno = dijkstra(grafoDijkstra, inicial)
	print("Noh inicial: ", inicial)
	print("Resultados do algorimo de Dijkstra:") 
	print("vertices [nome do vértice, distância, vértice anterior]: ", retorno)
	
	print("---------------------------------------------------------")
	print("Grafo usado para o algoritmo de Bellman-Ford: ")
	grafoBellmanFord.printAll()
	print("---------------------------------------------------------")
	inicial = grafoBellmanFord.vertices[0].getRotulo()
	
	
	print("---------------------------------------------------------")
	print("Algoritmo de Bellman-Ford")
	retorno = bellmanford(grafoBellmanFord, inicial)
	print(retorno)
	
	print("---------------------------------------------------------")
	print("Grafo usado para o algorimo de FloydWardshall: ")
	grafoFloydWarshall.printAll()
	print("---------------------------------------------------------")
	inicial = grafoFloydWarshall.vertices[0].getRotulo()
	
	
	print("---------------------------------------------------------")
	print("Algoritmo de FloydWardshall")
	retorno = floydWarshall(grafoFloydWarshall)
	print(retorno)
	
	pare = input('')

main() 
