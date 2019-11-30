''' Module that models a simple non-valued undirected graph as an adjacency matrix.'''

class Graph:

	def __init__(self, adjacency_matrix = list(), vertices_names = list()):
		if len(adjacency_matrix) != len(vertices_names):
			raise(Exception('Adjacency matrix and vertices names list must have the same order (length).'))
		else:
			self.vertices = vertices_names
			self.adjacency_matrix = adjacency_matrix


	# Checks if a vertex exists
	def vertex_exists(self, vertex):
		for v in self.vertices:
			if vertex == v:
				return True
		return False


	# Adds a new vertex
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


	# Adds a list of vertices
	def add_vertices(self, vertices_names):
		for vertex in vertices_names:
			self.add_vertex(vertex)


	# Adds a new edge between `vertex_a` and `vertex_b`
	def add_edge(self, vertex_a, vertex_b):
		self.adjacency_matrix[self.get_vertex_position(vertex_a)][self.get_vertex_position(vertex_b)] = 1
		self.adjacency_matrix[self.get_vertex_position(vertex_b)][self.get_vertex_position(vertex_a)] = 1


	# Sets a value to the corresponding edge
	def set_edge(self, index_i, index_j, value):
		if value in [0, 1]:
			self.adjacency_matrix[index_i][index_j] = value
		raise(ValueError('The value %d cant be set on the edges.' % value))


	# Returns the value of edge corresponding to `self.adjacency_matrix[index_i][index_j]`
	def get_edge(self, index_i, index_j):
		return self.adjacency_matrix[index_i][index_j]


	# Returns the vertices names list
	def get_vertices(self):
		return self.vertices


	# Given the vertex name, returns the position of the vertex
	def get_vertex_position(self, vertex):
		if self.vertex_exists(vertex):
			index = 0
			for v in self.vertices:
				if vertex == v:
					return index
				index += 1
		else:
			raise(Exception("Vertex %s doesn't exists." % vertex))


	# Given the vertex position, returns the name of the vertex
	def get_vertex_name(self, vertex_position):
		if 0 <= vertex_position < len(self.vertices):
			return self.vertices[vertex_position]
		else:
			raise(Exception("That vertex doesn't exists."))


	# Returns the `vertex` degree
	def vertex_degree(self, vertex):
		degree = 0
		for number in self.adjacency_matrix[self.get_vertex_position(vertex)]:
			degree += number
		return degree


	# Checks if a edge exists
	def edge_exists(self, vertex_a, vertex_b):
		return self.adjacency_matrix[self.get_vertex_position(vertex_a)][self.get_vertex_position(vertex_b)] == 1


	# Returns a list with the indexes of the adjacents vertices for `vertex`
	def get_adjacent_indexes(self, vertex):
		adjacent = list()
		index = 0
		for v in self.adjacency_matrix[self.get_vertex_position(vertex)]:
			if v == 1:
				adjacent.append(index)
			index += 1
		return adjacent


	# Returns a list with the names of the adjacents vertices for `vertex`
	def get_adjacent(self, vertex):
		adjacent = list()
		index = 0
		for v in self.adjacency_matrix[self.get_vertex_position(vertex)]:
			if v == 1:
				adjacent.append(self.vertices[index])
			index += 1
		return adjacent


	# Returns True if the `vertex` is adjacent to `vertices_list`
	def is_adjacent_to(self, vertex, vertices_list):
		for v in vertices_list:
			if not self.edge_exists(v, vertex):
				return False
		return True


	# Clears the set of edges and vertices of the graph
	def clear(self):
		self.vertices = list()
		self.adjacency_matrix = list()

	
	# Returns a list with edges `e` in form (a, b), where a and b are vertices
	# and each `e` forms a cycle in the graph, starting from `root`.
	def cycles(self, root):
		if not self.vertex_exists(root):
			raise(ValueError("This vertex does not exist."))
		cycles = list()
		for cycle in self.deep_first_search('', root, []):
			if cycle not in cycles and (cycle[1], cycle[0]) not in cycles:
				cycles.append(cycle)
		return cycles
	

	# Performs a deep-first search in the graph. Returns a list with the
	# back edges. Searches vertices only in the conex part.
	def deep_first_search(self, predecessor, root, marked):
		if not self.vertex_exists(root):
			raise(ValueError("This vertex does not exist."))
		marked.append(root)
		back_edges = list()
		for adj in self.get_adjacent(root):
			if adj not in marked:
				#print('Going from %s to %s with marked = %s' % (root, adj, marked))
				back_edges += self.deep_first_search(root, adj, marked)
			elif adj != predecessor:
				back_edges.append((root, adj))
		return back_edges


	# Returns the height of the graph
	def graph_height(self, root):
		if not self.vertex_exists(root):
			raise(ValueError("This vertex does not exist."))
		search = self.breadth_first_search(root)
		larger = search.pop()[1]
		for pair in search:
			if pair[1] > larger:
				larger = pair[1]
		return larger

	
	# Performs a breadth-first search in the graph. Returns a list with the
	# pairs (a, b) of each vertex, where each index `i` of the `depths` vector 
	# corresponds to respective vertex `i` on `self.vertices` vector. `a` is the 
	# predecessor and `b` is the depth of `self.vertices[i]`.  Searches vertices 
	# only in the conex part.
	def breadth_first_search(self, root):
		if not self.vertex_exists(root):
			raise(ValueError("This vertex does not exist."))
		# Starts the list with the depths of the vertices
		search = [('', 0) for _ in self.vertices]
		# Creates the queue and starts the search
		queue = [root]
		for vertex in queue:
			for adjacent in self.get_adjacent(vertex):
				if adjacent not in queue:
					#print('Going from %s to %s with depth = %s' % (vertex, adjacent, search[self.get_vertex_position(vertex)][1] + 1))
					queue.append(adjacent)
					search[self.get_vertex_position(adjacent)] = (vertex, search[self.get_vertex_position(vertex)][1] + 1)
		return search


	# Returns a list that contains the nodes connected to the `root` node 
	# directly and indirectly
	def conex_vertices(self, root):
		if not self.vertex_exists(root):
			raise(ValueError("This vertex does not exist."))
		connected_vertices = [root]
		index = 0
		for vertex in self.breadth_first_search(root):
			if vertex[1] != 0:
				connected_vertices.append(self.get_vertex_name(index))
			index += 1
		return connected_vertices



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
