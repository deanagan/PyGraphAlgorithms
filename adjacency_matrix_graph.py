#!/usr/bin/python3

from base_graph import Graph
import numpy as np

class AdjacencyMatrixGraph(Graph):
    def __init__(self, num_vertices, directed = False):
        super(AdjacencyMatrixGraph, self).__init__(num_vertices, directed)

        self.matrix = np.zeros((num_vertices, num_vertices))

    def add_edge(self, v1, v2, weight = 1):
        if v1 >= self.num_vertices or v2 >= self.num_vertices or v1 < 0 or v2 < 0:
            raise ValueError("Vertices out of bounds")

        if weight < 1:
            raise ValueError("Invalid weight")

        self.matrix[v1][v2] = weight

        if not self.directed:
            self.matrix[v2][v1] = weight

    def adjacent_vertices(self, v):
        if v < 0 or v >= self.num_vertices:
            raise ValueError("Cannot access vertex")

        return [i for i in range(self.num_vertices) if self.matrix[v][i] > 0]

    def edge_weight(self, v1, v2):
        return self.matrix[v1][v2]

    def in_degree(self, v):
        if v < 0 or v >= self.num_vertices:
            raise ValueError("Cannot access vertex")

        return len([i for i in range(self.num_vertices) if self.matrix[i][v] > 0])
