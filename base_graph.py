#!/usr/bin/python3

import abc

class Graph(abc.ABC):
    def __init__(self, num_vertices, directed = False):
        self.num_vertices = num_vertices
        self.directed = directed

    @abc.abstractmethod
    def add_edge(self, v1, v2, weight):
        pass

    @abc.abstractmethod
    def adjacent_vertices(self, v):
        pass

    @abc.abstractmethod
    def edge_weight(self, v1, v2):
        pass

    def display(self):
        vertex_pairs = [(i,v) for i in range(self.num_vertices) for v in self.adjacent_vertices(i)]
        for p in vertex_pairs:
            print(sep="-->", *p)

    ''' Number of directed edges flowing into node v '''
    @abc.abstractmethod
    def in_degree(self, v):
        pass

    # ToDo: Implement - has_cycle -> true if no node has in-degree == 0