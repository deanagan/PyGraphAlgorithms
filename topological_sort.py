
from queue import Queue
from base_graph import Graph

class TopologicalSort:
    def sort(self, graph):
        queue = Queue()
        indegree = dict()

        for i in range(graph.num_vertices):
            indegree[i] = graph.in_degree(i)

            if indegree[i] == 0:
                queue.put(i)

        result = []
        while not queue.empty():
            v = queue.get()
            result.append(v)
            for nv in graph.adjacent_vertices(v):
                indegree[nv] -= 1
                if indegree[nv] == 0:
                    queue.put(nv)

        if len(result) != graph.num_vertices:
            raise ValueError("Cycle detected")

        print(result)
