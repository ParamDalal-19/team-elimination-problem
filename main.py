from graph import Graph

graph = [
    [0, 1, 6, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, float('inf'), float('inf'), 0, 0],
    [0, 0, 0, 0, float('inf'), 0, float('inf'), 0],
    [0, 0, 0, 0, 0, float('inf'), float('inf'), 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 6],
    [0, 0, 0, 0, 0, 0, 0, 5],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

g = Graph(graph)

source = 0
sink = 7

print("Max Flow: %d " % g.ford_fulkerson(source, sink))
