from graph import Graph

g = Graph()
g.add_vertices(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
g.add_edge('A', 'B')
g.add_edge('B', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'E')
g.add_edge('D', 'E')
g.add_edge('E', 'G')
g.add_edge('F', 'G')
g.add_edge('B', 'F')

print(g)

g.cycles('A')
g.breadth_first_search('A')
g.graph_height('B')