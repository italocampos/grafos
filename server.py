# -*- coding: utf-8 -*-

from rpyc import Service
from rpyc.utils.server import ThreadedServer
from input import *
from algoritmos import *

class GraphService(Service):
	def on_connect(self, conn):
		print('A new client was connected: ')

	def on_disconnect(self, conn):
		print('A client was disconnected: ')

	def exposed_create_graph(self, string):
		graph = read_from_string(string)
		if graph:
			self.graph = graph
			return str(graph)
		else:
			return None

	def exposed_depth_first_search(self, initial_vertex):
		return buscaProfundidade(self.graph, initial_vertex, [], [], [])

	def exposed_prim(self, initial_vertex):
		return prim(self.graph, initial_vertex)

	def exposed_boruvka(self):
		return boruvka(self.graph)

	def exposed_dijkstra(self, initial_vertex):
		return dijkstra(self.graph, initial_vertex)

	def floydWarshall(self):
		return floydWarshall(self.graph)

	def exposed_show_graph(self):
		return str(self.graph)

if __name__ == "__main__":
	#ip, port = input('Inform the IP address and port where you want to run the server: ').split()
	#port = int(port)
	#t = ThreadedServer(GraphService, hostname=ip, port=port)
	t = ThreadedServer(GraphService, hostname='localhost', port=18861)
	print('GraphService initiated at {host}:{port}'.format(host = t.host, port = t.port))
	t.start()

#import rpyc
#conn = rpyc.connect('127.0.0.1', 18861)
#file = open('teste.in')
#string = file.read()
#ret = conn.root.create_graph()
#print(ret)