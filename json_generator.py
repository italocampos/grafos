#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import jsonpickle as jp
from input import *
from grafo import Grafo

file_name = input('Please, enter the input file name (like input.in): ')
graph = lerGrafo(file_name)
with open('graph.json', 'w') as outfile:
	json.dump(jp.encode(graph, unpicklable = False), outfile)