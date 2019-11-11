import pytest

from adjacency_matrix_graph import AdjacencyMatrixGraph

def setup():
    g = AdjacencyMatrixGraph(4, True)

    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(2, 3)

    return g

def test_adjacent():

    g = setup()
    assert(g.adjacent_vertices(0) == [1,2])
    assert(g.adjacent_vertices(1) == [])
    assert(g.adjacent_vertices(2) == [3])
    assert(g.adjacent_vertices(3) == [])

def test_indegree():
    g = setup()

    assert(g.in_degree(0) == 0)
    assert(g.in_degree(1) == 1)
    assert(g.in_degree(2) == 1)
    assert(g.in_degree(3) == 1)

def test_edgeweight():
    g = setup()

    for i in range(4):
        for j in g.adjacent_vertices(i):
            assert(1.0 == g.edge_weight(i,j))