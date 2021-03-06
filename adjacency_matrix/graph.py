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
		self.set_edge(self.get_vertex_index(vertex_a), self.get_vertex_index(vertex_b), 1)

	
	# Removes an edge between `vertex_a` and `vertex_b`
	def remove_edge(self, vertex_a, vertex_b):
		self.set_edge(self.get_vertex_index(vertex_a), self.get_vertex_index(vertex_b), 0)


	# Sets a value (0 or 1) to the corresponding edge
	def set_edge(self, index_i, index_j, value):
		if 0 <= index_i < len(self.adjacency_matrix) and 0 <= index_j < len(self.adjacency_matrix):
			if value in [0, 1]:
				self.adjacency_matrix[index_i][index_j] = value
				self.adjacency_matrix[index_j][index_i] = value
			else:
				raise(ValueError('The value %d cant be set on the edges.' % value))
		else:
			raise(ValueError('This edge does not exist.'))


	# Returns the value of edge corresponding to `self.adjacency_matrix[index_i][index_j]`
	def get_edge(self, index_i, index_j):
		return self.adjacency_matrix[index_i][index_j]


	# Returns the vertices names list
	def get_vertices(self):
		return self.vertices


	# Given the vertex name, returns the position of the vertex
	def get_vertex_index(self, vertex):
		if self._is_valid_vertex(vertex):
			index = 0
			for v in self.vertices:
				if vertex == v:
					return index
				index += 1


	# Given the vertex position, returns the name of the vertex
	def get_vertex_name(self, vertex_position):
		if 0 <= vertex_position < len(self.vertices):
			return self.vertices[vertex_position]
		else:
			raise(Exception("That vertex doesn't exist."))


	# Returns the `vertex` degree
	def vertex_degree(self, vertex):
		degree = 0
		for number in self.adjacency_matrix[self.get_vertex_index(vertex)]:
			degree += number
		return degree


	# Checks if a edge exists
	def edge_exists(self, vertex_a, vertex_b):
		return self.adjacency_matrix[self.get_vertex_index(vertex_a)][self.get_vertex_index(vertex_b)] == 1


	# Returns a list with the indexes of the adjacents vertices for `vertex`
	def get_adjacent_indexes(self, vertex):
		adjacent = list()
		index = 0
		for v in self.adjacency_matrix[self.get_vertex_index(vertex)]:
			if v == 1:
				adjacent.append(index)
			index += 1
		return adjacent


	# Returns a list with the names of the adjacents vertices for `vertex`
	def get_adjacent(self, vertex):
		adjacent = list()
		index = 0
		for v in self.adjacency_matrix[self.get_vertex_index(vertex)]:
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
	# and each `e` is a back edge in the graph, starting from `root`.
	def deep_first_search(self, root):
		back_edges = list()
		for be in self._dfs('', root, []):
			if be not in back_edges and (be[1], be[0]) not in back_edges:
				back_edges.append(be)
		return back_edges
	

	# Performs a deep-first search in the graph. Returns a list with the
	# back edges. Searches vertices only in the conex part.
	def _dfs(self, predecessor, root, marked):
		if self._is_valid_vertex(root):
			marked.append(root)
			back_edges = list()
			for adj in self.get_adjacent(root):
				if adj not in marked:
					#print('Going from %s to %s with marked = %s' % (root, adj, marked))
					back_edges += self._dfs(root, adj, marked)
				elif adj != predecessor:
					back_edges.append((root, adj))
			return back_edges


	# Returns a list with the back_edges found using the seleted search method.
	# The available methos are: 'dfs' (deep-first search) and 'bfs' (breadth-first)
	# search
	def cycles(self, root, search = 'dfs'):
		if search == 'dfs':
			return self.deep_first_search(root)
		if search == 'bfs':
			_, be = self.breadth_first_search(root)
			back_edges = list()
			for b in be:
				if b not in back_edges and (b[1], b[0]) not in back_edges:
					back_edges.append(b)
			return back_edges


	# Returns the height of the graph
	def height(self, root):
		search, _ = self.breadth_first_search(root)
		larger = search.pop()[1]
		for pair in search:
			if pair[1] > larger:
				larger = pair[1]
		return larger

	
	# Performs a breadth-first search in the graph. Returns two lists. The first
	# one list with the pairs (a, b) of each vertex, where each index `i` of the
	# returned `search` vector corresponds to the respective vertex `i` on 
	# `self.vertices` vector. `a` is the predecessor and `b` is the depth of 
	# `self.vertices[i]`. The second one list has the found back edges. This 
	# method searches vertices only in the conex part of the graph.
	def breadth_first_search(self, root):
		if self._is_valid_vertex(root):
			# List with the back edges
			back_edges = list()
			# Starts the list with the depths of the vertice
			search = [('', 0) for _ in self.vertices]
			# Creates the queue and starts the search
			queue = [root]
			for vertex in queue:
				for adjacent in self.get_adjacent(vertex):
					if adjacent not in queue:
						#print('Going from %s to %s with depth = %s' % (vertex, adjacent, search[self.get_vertex_index(vertex)][1] + 1))
						queue.append(adjacent)
						search[self.get_vertex_index(adjacent)] = (vertex, search[self.get_vertex_index(vertex)][1] + 1)
					elif adjacent != search[self.get_vertex_index(vertex)][0]:
						back_edges.append((vertex, adjacent))
			return search, back_edges


	# Returns a list that contains the nodes connected to the `root` node 
	# directly and indirectly
	def conex_vertices(self, root):
		connected_vertices = [root]
		index = 0
		found_vertices, _ = self.breadth_first_search(root)
		for vertex in found_vertices:
			if vertex[1] != 0:
				connected_vertices.append(self.get_vertex_name(index))
			index += 1
		return connected_vertices


	def _is_valid_vertex(self, vertex):
		if self.vertex_exists(vertex):
			return True
		raise(Exception("The vertex %s doesn't exist." % vertex))


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
