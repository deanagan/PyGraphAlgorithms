from adjacency_matrix_graph import AdjacencyMatrixGraph
from adjacency_set_graph import AdjacencySetGraph
from topological_sort import TopologicalSort
from unweighted_shortest_path import UnweightedShortestPath
from dijkstra_algorithm import DijkstraAlgorithm

if __name__ == "__main__":

    g = AdjacencyMatrixGraph(4, True)

    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(2, 3)

    for i in range(4):
        print("Adjacent to: ", i, g.adjacent_vertices(i))

    for i in range(4):
        print("In-degree: ", i, g.in_degree(i))

    for i in range(4):
        for j in g.adjacent_vertices(i):
            print("Edge Weight:", i, j, "weight", g.edge_weight(i,j))

    g.display()

    g2 = AdjacencySetGraph(4, False)

    g2.add_edge(0, 1)
    g2.add_edge(0, 2)
    g2.add_edge(2, 3)

    for i in range(4):
        print("Adjacent to: ", i, g2.adjacent_vertices(i))

    for i in range(4):
        print("In-degree: ", i, g2.in_degree(i))

    for i in range(4):
        for j in g2.adjacent_vertices(i):
            print("Edge Weight:", i, j, "weight", g2.edge_weight(i,j))

    g2.display()


    ts = TopologicalSort()

    g3 = AdjacencyMatrixGraph(9, True)
    g3.add_edge(0,1)
    g3.add_edge(1,2)
    g3.add_edge(2,7)
    g3.add_edge(2,4)
    g3.add_edge(2,3)
    g3.add_edge(1,5)
    g3.add_edge(5,6)
    g3.add_edge(3,6)
    g3.add_edge(3,4)
    g3.add_edge(6,8)

    ts.sort(g3)


    g4 = AdjacencyMatrixGraph(8)
    g4.add_edge(0,1)
    g4.add_edge(1,2)
    g4.add_edge(1,3)
    g4.add_edge(2,3)
    g4.add_edge(1,4)
    g4.add_edge(3,5)
    g4.add_edge(5,4)
    g4.add_edge(3,6)
    g4.add_edge(6,7)
    g4.add_edge(0,7)

    usp = UnweightedShortestPath(g4)
    usp.path(0, 5)
    usp.path(0, 6)
    usp.path(7, 4)

    g5 = AdjacencyMatrixGraph(8)
    g5.add_edge(0,1)
    g5.add_edge(1,2)
    g5.add_edge(1,3)
    g5.add_edge(2,3)
    g5.add_edge(1,4)
    g5.add_edge(3,5)
    g5.add_edge(5,4)
    g5.add_edge(3,6)
    g5.add_edge(6,7)
    g5.add_edge(0,7)

    # da = DijkstraAlgorithm(g5)
    # da.path(0, 5)
    # da.path(0, 6)
    # da.path(7, 4)

    g6 = AdjacencyMatrixGraph(6, True)
    g6.add_edge(0,1,1)
    g6.add_edge(0,5,7)
    g6.add_edge(1,2,1)
    g6.add_edge(1,3,3)
    g6.add_edge(1,4,1)
    g6.add_edge(2,3,1)
    g6.add_edge(3,5,2)
    g6.add_edge(5,4,1)

    best_path_to_5_is_01235 = DijkstraAlgorithm(g6)
    best_path_to_5_is_01235.path(0,5)
