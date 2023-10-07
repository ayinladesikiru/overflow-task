from challenge1.challenge_1b import Graph, identify_router


def test_identify_router_2():
    graph = Graph()
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 5)
    graph.add_edge(5, 2)
    graph.add_edge(2, 1)
    assert identify_router(graph) == [2]


def test_identify_router_5():
    graph = Graph()
    graph.add_edge(1, 3)
    graph.add_edge(3, 5)
    graph.add_edge(5, 6)
    graph.add_edge(6, 4)
    graph.add_edge(4, 5)
    graph.add_edge(5, 2)
    graph.add_edge(2, 6)
    assert identify_router(graph) == [5]


def test_identify_router_2_6():
    graph = Graph()
    graph.add_edge(2, 4)
    graph.add_edge(4, 6)
    graph.add_edge(6, 2)
    graph.add_edge(2, 5)
    graph.add_edge(5, 6)
    assert identify_router(graph) == [2, 6]

