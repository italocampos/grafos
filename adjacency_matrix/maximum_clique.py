from graph import Graph

def remove_sublist(list_, sublist):
	for element in sublist:
		list_.remove(element)

graph = Graph()
graph.read_from_file('sub4.in')

maximal_clique = list()

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