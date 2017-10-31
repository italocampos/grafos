#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tabela import Tabela
from input import *
from grafos import *
#import input.in

def main():
    a = Tabela()
    a = addFromFile('input.in')
    print("BUSCA EM GRAFOS +++++++++++++++++")
    print("INSTRUÇÕES: Para inserir um grafo no aplicativo, edite o arquivo input.in\
(no formato-exemplo em que está) neste diretório. O software utiliza a notação de\
listas de adjacências para representar grafos. ")
    print("\nGrafo lido:")
    a.printTable()
    
    buscaLargura(a, 1)

    print("---------------------------------------------------------")
    print("Busca em profundidade")
    marcados, explorados, retorno = buscaProfundidade(a, 1, [], [], [])
    print("Resultados da busca em profundidade:")
    print("Noh inicial: ", 1)
    print("Arestas exploradas: ", explorados)
    print("Arestas de retorno: ", retorno)
main()
