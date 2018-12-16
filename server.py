# -*- coding: utf-8 -*-

from rpyc import Service
from rpyc.utils.server import ThreadedServer
from input import *
from algoritmos import *

class GraphService(Service):
	def on_connect(self, port):
		print('New client connected: ', port)

	def on_disconnect(self, conn):
		print('The client was disconnected')

	def exposed_get_graph(self, string):
		graph = read_from_string(string)
		graph.print()

	#exposed_the_real_answer_though = 43     # an exposed attribute

	def get_question(self):  # while this method is not exposed
		return "what is the airspeed velocity of an unladen swallow?"

if __name__ == "__main__":
	t = ThreadedServer(GraphService, port=18861)
	t.start()