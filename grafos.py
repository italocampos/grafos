#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def isExplorado(exploradas, aresta):
    if [aresta[0],aresta[1]] in exploradas: return True
    if [aresta[1],aresta[0]] in exploradas: return True
    return False

def buscaProfundidade(grafo, no, marcados, explorados, retorno):
    marcados.append(no)
    for item in grafo.getAdjacentes(no):
        if item not in marcados:
            explorados.append([no,item])
            marcados.append(no)
            marcados, explorados, retorno = buscaProfundidade(grafo, item, marcados, explorados, retorno)
        else:
            if not isExplorado(explorados, [no,item]):
                explorados.append([no,item])
                retorno.append([no,item])
    return marcados, explorados, retorno

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
    print("---------------------------------------------------------")
    print("Resultados da busca em largura no grafo:")
    print("Noh inicial: ", vertice_inicial)
    print("Arestas exploradas: ", exploradas)
    print("Arestas de retorno: ", retorno, "\n")