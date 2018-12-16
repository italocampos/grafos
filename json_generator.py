#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from input import *
from grafo import Grafo

file_name = input('Please, enter the input file name (like input.in): ')
graph = lerGrafo(file_name)
with open('graph.json', 'w') as outfile:
	json.dump(graph.getJson(), outfile)