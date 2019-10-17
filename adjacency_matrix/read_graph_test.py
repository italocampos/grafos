from adjacency_matrix import Graph

g = Graph()

g.add_vertex('A')
g.add_vertices(['B', 'C', 'D'])

g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('A', 'D')
g.add_edge('B', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'D')

print(g.vertex_degree('C'))
print(g.vertex_degree('A'))

print(g.edge_exists('A', 'B'))
print(g.edge_exists('B', 'D'))

print(g.get_adjacent('B'))

print(g)

g.read_from_file('matrix.in')

print(g)