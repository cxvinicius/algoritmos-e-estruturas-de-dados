from estruturas.graphs.graph import Graph


def test_add_vertex():
    graph = Graph()

    graph.add_vertex("A")

    assert graph.has_vertex("A")
    assert len(graph) == 1


def test_add_duplicate_vertex():
    graph = Graph()

    graph.add_vertex("A")
    graph.add_vertex("A")

    assert len(graph) == 1


def test_add_edge_creates_vertices():
    graph = Graph()

    graph.add_edge("A", "B")

    assert graph.has_vertex("A")
    assert graph.has_vertex("B")
    assert len(graph) == 2


def test_add_edge_in_undirected_graph():
    graph = Graph()

    graph.add_edge("A", "B")

    assert graph.has_edge("A", "B")
    assert graph.has_edge("B", "A")


def test_add_edge_in_directed_graph():
    graph = Graph(directed=True)

    graph.add_edge("A", "B")

    assert graph.has_edge("A", "B")
    assert not graph.has_edge("B", "A")


def test_has_vertex():
    graph = Graph()

    graph.add_vertex("A")

    assert graph.has_vertex("A")
    assert not graph.has_vertex("B")


def test_has_edge():
    graph = Graph()

    graph.add_edge("A", "B")

    assert graph.has_edge("A", "B")
    assert not graph.has_edge("A", "C")
    assert not graph.has_edge("C", "A")


def test_get_neighbors():
    graph = Graph()

    graph.add_edge("A", "C")
    graph.add_edge("A", "B")

    assert graph.get_neighbors("A") == {"B", "C"}


def test_get_neighbors_from_nonexistent_vertex():
    graph = Graph()

    assert graph.get_neighbors("A") == set()


def test_get_neighbors_returns_copy():
    graph = Graph()

    graph.add_edge("A", "B")

    neighbors = graph.get_neighbors("A")
    neighbors.add("C")

    assert graph.get_neighbors("A") == {"B"}


def test_len():
    graph = Graph()

    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")

    assert len(graph) == 3


def test_contains():
    graph = Graph()

    graph.add_vertex("A")

    assert "A" in graph
    assert "B" not in graph


def test_breadth_first_search():
    graph = Graph(directed=True)

    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("C", "E")

    result = graph.breadth_first_search("A")

    assert result[0] == "A"
    assert set(result) == {"A", "B", "C", "D", "E"}
    assert result.index("A") < result.index("B")
    assert result.index("A") < result.index("C")
    assert result.index("B") < result.index("D")
    assert result.index("C") < result.index("E")


def test_breadth_first_search_from_nonexistent_vertex():
    graph = Graph()

    assert graph.breadth_first_search("A") == []


def test_depth_first_search():
    graph = Graph(directed=True)

    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("C", "E")

    assert graph.depth_first_search("A") == ["A", "B", "D", "C", "E"]


def test_depth_first_search_from_nonexistent_vertex():
    graph = Graph()

    assert graph.depth_first_search("A") == []