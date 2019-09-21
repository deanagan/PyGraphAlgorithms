from queue import Queue
from base_graph import Graph
from base_shortest_path_algorithm import BaseShortestPath

class UnweightedShortestPath(BaseShortestPath):
    def __init__(self, graph):
        super(UnweightedShortestPath, self).__init__(graph)

    def build_distance_table(self, source):
        q = Queue()
        q.put(source)
        distance_table = self.get_initial_distance_table(source)

        while not q.empty():
            v = q.get()
            distance = distance_table[v].distance
            for adjacent in self.graph.adjacent_vertices(v):
                # Unvisited vertices have distance = None
                if distance_table[adjacent].distance is None:
                    distance_table[adjacent].distance = distance + 1
                    distance_table[adjacent].preceding_vertex = v

                    # enqueue adjacent vertex if it has more adjacent vertices
                    if len(self.graph.adjacent_vertices(adjacent)) > 0:
                        q.put(adjacent)
        return distance_table
