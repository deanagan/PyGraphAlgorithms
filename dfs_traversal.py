from adjacency_matrix_graph import AdjacencyMatrixGraph
import numpy as np

class DfsTraversal:
    def __init__(self, graph):
        self.visited = np.zeros(graph.num_vertices)
        self.graph = graph

    def traverse(self, current=0):
        if self.visited[current] == 1:
            return
        self.visited[current] = 1

        print("Visit:", current)

        for vertex in self.graph.adjacent_vertices(current):
            self.traverse(vertex)

if __name__ == "__main__":
    g = AdjacencyMatrixGraph(6)

    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 5)

    dfs = DfsTraversal(g)

    dfs.traverse()