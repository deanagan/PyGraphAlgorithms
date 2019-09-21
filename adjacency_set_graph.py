#!/usr/bin/python3

from base_graph import Graph
import numpy as np


class Node:
    def __init__(self, vertex):
        self.vertex = vertex
        self.adjacency_set = set()

    def add_edge(self, v):
        if self.vertex == v:
            raise ValueError("No adjacency to self allowed")

        self.adjacency_set.add(v)

    def adjacent_vertices(self):
        return self.adjacency_set

class AdjacencySetGraph(Graph):
    def __init__(self, num_vertices, directed = False):
        super(AdjacencySetGraph, self).__init__(num_vertices, directed)
        self.vertex_list = [Node(i) for i in range(num_vertices)]

    def add_edge(self, v1, v2, weight = 1):
        if v1 >= self.num_vertices or v2 >= self.num_vertices or v1 < 0 or v2 < 0:
            raise ValueError("Vertices out of bounds")

        if weight != 1:
            raise ValueError("Adjacency sets only represent 1 as edge weights")

        self.vertex_list[v1].add_edge(v2)

        if not self.directed:
            self.vertex_list[v2].add_edge(v1)

    def adjacent_vertices(self, v):
        if v < 0 or v >= self.num_vertices:
            raise ValueError("Cannot access vertex")

        return self.vertex_list[v].adjacent_vertices()

    def edge_weight(self, v1, v2):
        return 1

    def in_degree(self, v):
        if v < 0 or v >= self.num_vertices:
            raise ValueError("Cannot access vertex")

        return len([i for i in range(self.num_vertices) if v in self.adjacent_vertices(i)])
