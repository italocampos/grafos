from graph import Graph

def remove_sublist(list_, sublist):
	for element in sublist:
		list_.remove(element)

graph = Graph()
graph.read_from_file('k26.in')


def merge(vector_a, vector_b):
	merged = list()
	for _ in range(len(vector_a)):
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


maximal_clique = list()

''' Version 1.0 (wrong)
for vertex in graph.get_vertices():
	adjacent = graph.get_adjacent(vertex)
	not_clique = list()
	begin = 1
	for line in adjacent:
		if line in not_clique:
			break
		for column in adjacent[begin:]:
			if graph.get_edge(line, column) == 0:
				#print('Do not compound the clique with %s: %d' % (vertex, line))
				not_clique.append(line)
				break
		begin += 1

	remove_sublist(adjacent, not_clique)
	adjacent.insert(0, graph.get_vertex_position(vertex))
	maximal_clique.append(adjacent)

print(maximal_clique)

maximum_clique = maximal_clique.pop(0)
for clique in maximal_clique:
	if len(clique) > len(maximum_clique):
		maximum_clique = clique

print('Maximum clique %d found at: ' % len(maximum_clique), end = '')
for vertex in maximum_clique:
	print(graph.get_vertex_name(vertex), ' ', end = '')
print()
'''

for vertex in graph.get_vertices():
	adjacent = graph.get_adjacent(vertex)
	
	# Create the degree list to adjacent vertex
	degrees = list()
	for line in adjacent:
		degree_sum = 0
		for column in adjacent:
			if graph.edge_exists(line, column):
				degree_sum += 1
		degrees.append((line, degree_sum))

	# Sort the adjacent vertices by degree
	degrees = merge_sort(degrees)

	# Adds the adjacent with greater degree to the clique, while possible
	clique = [vertex, degrees.pop(0)[0]]
	for candidate in degrees:
		if graph.is_adjacent_to(candidate[0], clique):
			clique.append(candidate[0])

	maximal_clique.append(clique)

	
#print('Maximal clique list:', maximal_clique)

maximum_clique = maximal_clique.pop(0)
for clique in maximal_clique:
	if len(clique) > len(maximum_clique):
		maximum_clique = clique

print('Maximum clique %d found at: ' % len(maximum_clique), end = '')
print(maximum_clique)