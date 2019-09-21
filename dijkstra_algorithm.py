
# Difference to unweighted shortest path
# 1. Prefer this method when dealing with weighted edges as it enqueues neighbours based on the edge weight.
# 2. Calculates distance by adding weights.
# 3. Recalculates distance to visited nodes, updating if needed.
# 4. Re-enqueue distance if it is updated.
from queue import Queue
from base_graph import Graph
from collections import deque
from base_shortest_path_algorithm import BaseShortestPath
from heapq import heappush, heappop


class DistanceVertexPair:
    def __init__(self, distance, vertex):
        self.distance = distance
        self.vertex = vertex

    def __lt__(self, other):
        return self.distance < other.distance

    def __eq__(self, other):
	    return self.distance == other.distance

    def __str__(self):
        return "Vertex{} Distance{}".format(self.vertex, int(self.distance) if not None else "inf")

class DijkstraAlgorithm(BaseShortestPath):
    def __init__(self, graph):
        super(DijkstraAlgorithm, self).__init__(graph)

    def build_distance_table(self, source):
        distance_table = self.get_initial_distance_table(source)

        pq = []
        heappush(pq, DistanceVertexPair(0, source))
        while len(pq):
            dvp = heappop(pq)
            distance = distance_table[dvp.vertex].distance
            for adjacent_vertex in self.graph.adjacent_vertices(dvp.vertex):
                total_distance = distance + self.graph.edge_weight(dvp.vertex, adjacent_vertex)
                distance_from_origin = distance_table[adjacent_vertex].distance

                if distance_from_origin is None or distance_from_origin > total_distance:
                    distance_table[adjacent_vertex].distance = total_distance
                    distance_table[adjacent_vertex].preceding_vertex = dvp.vertex
                    heappush(pq, DistanceVertexPair(total_distance, adjacent_vertex))

        return distance_table
