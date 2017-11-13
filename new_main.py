#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# from tabela import Tabela
from grafo import Grafo

def main():
    a = Grafo()
    a.addVertice(1)
    a.addVertice(2)
    a.addAresta([1,2])
    a.print()

main()