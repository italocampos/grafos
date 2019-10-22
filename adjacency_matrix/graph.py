''' Module that models a simple non-valued undirected graph as an adjacency matrix.'''

class Graph:

	def __init__(self, adjacency_matrix = list(), vertices_names = list()):
		if len(adjacency_matrix) != len(vertices_names):
			raise(Exception('Adjacency matrix and vertices names list must have the same order (length).'))
		else:
			self.vertices = vertices_names
			self.adjacency_matrix = adjacency_matrix


	def vertex_exists(self, vertex):
		for v in self.vertices:
			if vertex == v:
				return True
		return False


	def add_vertex(self, vertex_name):
		if not self.vertex_exists(vertex_name):
			for line in self.adjacency_matrix:
				line.append(0);
			self.vertices.append(vertex_name)
			adjacent = list()
			for _ in self.vertices:
				adjacent.append(0)
			self.adjacency_matrix.append(adjacent)
		else:
			raise(Exception('Vertex %s already exists.' % vertex_name))


	def add_vertices(self, vertices_names):
		for vertex in vertices_names:
			self.add_vertex(vertex)


	def add_edge(self, vertex_a, vertex_b):
		self.adjacency_matrix[self.get_vertex_position(vertex_a)][self.get_vertex_position(vertex_b)] = 1
		self.adjacency_matrix[self.get_vertex_position(vertex_b)][self.get_vertex_position(vertex_a)] = 1


	def set_edge(self, index_i, index_j, value):
		self.adjacency_matrix[index_i][index_j] = value

	def get_edge(self, index_i, index_j):
		return self.adjacency_matrix[index_i][index_j]


	def get_vertices(self):
		return self.vertices


	def get_vertex_position(self, vertex):
		if self.vertex_exists(vertex):
			index = 0
			for v in self.vertices:
				if vertex == v:
					return index
				index += 1
		else:
			raise(Exception("Vertex %s doesn't exists." % vertex))


	def get_vertex_name(self, vertex_position):
		if 0 <= vertex_position < len(self.vertices):
			return self.vertices[vertex_position]
		else:
			raise(Exception("That vertex doesn't exists."))


	def vertex_degree(self, vertex):
		degree = 0
		for number in self.adjacency_matrix[self.get_vertex_position(vertex)]:
			degree += number
		return degree


	def edge_exists(self, vertex_a, vertex_b):
		return self.adjacency_matrix[self.get_vertex_position(vertex_a)][self.get_vertex_position(vertex_b)] == 1


	def get_adjacent(self, vertex):
		adjacent = list()
		index = 0
		for v in self.adjacency_matrix[self.get_vertex_position(vertex)]:
			if v == 1:
				adjacent.append(index)
			index += 1
		return adjacent


	def clear(self):
		self.vertices = list()
		self.adjacency_matrix = list()


	def read_from_file(self, file_name):
		self.clear()
		file = open(file_name, 'r')
		for vertex_name in file.readline().splitlines()[0].split('\t'):
			self.add_vertex(vertex_name)
			#print(vertex_name)
		i = 0
		for line in file:
			j = 0
			for number in line.split('\t'):
				#print('(%d, %d): %s' % (i, j, number))
				self.set_edge(i, j, int(number))
				j += 1
			i += 1
		file.close()

	def __str__(self):
		#string = '   '
		string = '\t'
		for vertex_name in self.vertices:
			#string += vertex_name + '   '
			string += vertex_name + '\t'
		string += '\n'
		index = 0
		for line in self.adjacency_matrix:
			#string += self.vertices[index] + '  '
			string += self.vertices[index] + '\t'
			for number in line:
				#string += str(number) + '   '
				string += str(number) + '\t'
			string += '\n'
			index += 1
		return string