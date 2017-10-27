#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tabela import Tabela

def main():
    a = Tabela()
    a.addLinha('1 -> 2, 3')
    a.addLinha('2 -> 1, 3')
    a.addLinha('3 -> 1, 2, 4, 5, 6, 7')
    a.addLinha('4 -> 3, 5')
    a.addLinha('5 -> 3, 4')
    a.addLinha('6 -> 3')
    a.addLinha('7 -> 3')
    a.addLinha(1)
    a.printTable()
    m, e = deepSearch(a, '1', [], [])
    print('Nos marcados: ', m)
    print('Nos explorados: ', e)
main()
