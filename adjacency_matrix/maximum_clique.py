from graph import Graph
from tools import convert_graph, merge_sort

#graph = Graph()
#graph.read_from_file('input/k26.in')
graph = convert_graph('input/graph_250.in')


maximal_clique = list()


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