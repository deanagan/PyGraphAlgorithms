from queue import Queue
from adjacency_matrix_graph import AdjacencyMatrixGraph
import numpy as np


class BfsTraversal:
    def traverse(self, graph, start=0):
        queue = Queue()
        queue.put(start)

        visited = np.zeros(graph.num_vertices)

        while not queue.empty():
            vertex = queue.get()

            if visited[vertex] == 1:
                continue

            print("Visit:", vertex)

            visited[vertex] = 1

            new_items = (v for v in graph.adjacent_vertices(vertex) if visited[v] != 1)
            for item in new_items:
                queue.put(item)



if __name__ == "__main__":
    g = AdjacencyMatrixGraph(6)

    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 5)

    bfs = BfsTraversal()

    bfs.traverse(g)
