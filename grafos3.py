#!/usr/bin/env python3

def isExplorado(marcados, a, b):
    if (str(a) + '-' + str(b)) in marcados: return True
    if (str(b) + '-' + str(a)) in marcados: return True
    if ('retorno - ' + str(a) + '-' + str(b)) in marcados: return True
    if ('retorno - ' + str(b) + '-' + str(a)) in marcados: return True
    return False

def deepSearch(grafo, no, marcados, explorados):
    marcados.append(str(no))
    #for item in grafo.getLine(int(no))[1:]:
    print("DEBUG 1: ", grafo.getLine(grafo.elementIndex(no)))
    print("DEBUG 2: ", grafo.lista[grafo.elementIndex(no)])
    for item in grafo.lista[grafo.elementIndex(no)][1:]:
        if str(item) not in marcados:
            explorados.append(str(no) + '-' + str(item))
            marcados, explorados = deepSearch(grafo, str(item), marcados, explorados)
        else:
            if not isExplorado(explorados, str(no), str(item)):
                explorados.append('retorno - ' + str(no) + '-' + str(item))
    return marcados, explorados