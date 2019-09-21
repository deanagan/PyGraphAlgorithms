
import abc
from collections import deque

class DistanceTableEntry:
    def __init__(self, distance = None, preceding_vertex = None):
        self.distance = distance
        self.preceding_vertex = preceding_vertex

class BaseShortestPath(abc.ABC):
    def __init__(self, graph):
        self.graph = graph

    @abc.abstractmethod
    def build_distance_table(self, source):
        pass

    ''' A path to destination is determined thru backtracking '''
    def path(self, source, destination):
        distance_table = self.build_distance_table(source)
        path = deque([destination])
        prev_vertex = distance_table[destination].preceding_vertex

        while prev_vertex is not None and prev_vertex is not source:
            path.appendleft(prev_vertex)
            prev_vertex = distance_table[prev_vertex].preceding_vertex

        if prev_vertex is None:
            print("No path to destination")
        else:
            path.appendleft(source)

        print(path)

    def get_initial_distance_table(self, source):
        distance_table = dict()

        for i in range(self.graph.num_vertices):
            distance_table[i] = DistanceTableEntry(0, source) if i == source else DistanceTableEntry()

        return distance_table

    def show(self, distance_table):
        for i in range(len(distance_table)):
            print(i, int(distance_table[i].distance) if not distance_table[i].distance is None else "inf", distance_table[i].preceding_vertex)
        print()