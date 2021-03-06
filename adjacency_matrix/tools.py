from graph import Graph

def convert_graph(file_name):
	file = open(file_name, 'r')
	g = Graph()

	for line in file:
		if line != '\n':
			a, b = line.split()
			#a, b = int(a), int(b)
			
			if not g.vertex_exists(a):
				g.add_vertex(a)
			if not g.vertex_exists(b):
				g.add_vertex(b)
			g.add_edge(a, b)

	return g


def remove_sublist(list_, sublist):
	for element in sublist:
		list_.remove(element)


def merge(vector_a, vector_b):
	merged = list()
	while vector_a != [] and vector_b != []:
		if vector_a[0][1] > vector_b[0][1]:
			merged.append(vector_a.pop(0))
		else:
			merged.append(vector_b.pop(0))
	merged += vector_a + vector_b
	return merged


# Sort a list under form [('VERTEX', degree), ...] in a descending order
def merge_sort(vector):
	if len(vector) in [0, 1]:
		return vector
	else:
		vector_a = merge_sort(vector[:len(vector)//2])
		vector_b = merge_sort(vector[len(vector)//2:])
		return merge(vector_a, vector_b)


# Read a adjacency matrix from a file and returns a Graph object
def read_from_file(file_name):
	g = Graph()
	g.clear()
	file = open(file_name, 'r')
	for vertex_name in file.readline().splitlines()[0].split('\t'):
		g.add_vertex(vertex_name)
		#print(vertex_name)
	i = 0
	for line in file:
		j = 0
		for number in line.split('\t'):
			#print('(%d, %d): %s' % (i, j, number))
			g.set_edge(i, j, int(number))
			j += 1
		i += 1
	file.close()
	return g
