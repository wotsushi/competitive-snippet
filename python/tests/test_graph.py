from snippets.graph import (
    bellman_ford,
    dijkstra,
    prim,
    warshall_floyd,
    topological_sort,
    readgraph,
    readdirectedgraph,
    readweightedgraph,
    readweighteddirectedgraph
)
from tests.data_graph import (
    K4,
    sparse_graph,
    no_edge_graph,
    d_K4,
    d_sparse_graph,
    w_K4,
    w_sparse_graph,
    w_no_edge_graph,
    wd_K4,
    wd_sparse_graph,
    wd_negative_weight_graph,
    wd_zero_weight_graph,
    dag_line,
    dag_binary_tree,
    dag_star,
    dag_grid
)
from parameterized import parameterized

INF = 10**3


@parameterized.expand(
    [
        (
            4,
            [1, 2, 3, 1, 2, 1],
            [2, 3, 4, 3, 4, 4],
            K4
        ),
        (
            10,
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            [2, 3, 4, 5, 6, 7, 8, 9, 10, 1],
            sparse_graph
        ),
        (
            3,
            [],
            [],
            no_edge_graph
        )
    ]
)
def test_readgraph(N, a, b, expected):
    actual = readgraph.code(N, a, b)
    assert actual == expected


@parameterized.expand(
    [
        (
            4,
            [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4],
            [2, 3, 4, 1, 3, 4, 1, 2, 4, 1, 2, 3],
            d_K4
        ),
        (
            10,
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            [2, 3, 4, 5, 6, 7, 8, 9, 10, 1],
            d_sparse_graph
        ),
        (
            3,
            [],
            [],
            no_edge_graph
        )
    ]
)
def test_readdirectedgraph(N, a, b, expected):
    actual = readdirectedgraph.code(N, a, b)
    assert actual == expected


@parameterized.expand(
    [
        (
            4,
            [1, 2, 3, 1, 2, 1],
            [2, 3, 4, 3, 4, 4],
            [1, 1, 2, 3, 5, 8],
            w_K4
        ),
        (
            10,
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            [2, 3, 4, 5, 6, 7, 8, 9, 10, 1],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            w_sparse_graph
        ),
        (
            3,
            [],
            [],
            [],
            w_no_edge_graph
        )
    ]
)
def test_readweightedgraph(N, a, b, c, expected):
    actual = readweightedgraph.code(N, a, b, c)
    assert actual == expected


@parameterized.expand(
    [
        (
            4,
            [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4],
            [2, 3, 4, 1, 3, 4, 1, 2, 4, 1, 2, 3],
            [1, 3, 8, 1, 1, 5, 3, 1, 2, 8, 5, 2],
            wd_K4
        ),
        (
            10,
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            [2, 3, 4, 5, 6, 7, 8, 9, 10, 1],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            wd_sparse_graph
        ),
        (
            3,
            [],
            [],
            [],
            w_no_edge_graph
        )
    ]
)
def test_readweighteddirectedgraph(N, a, b, c, expected):
    actual = readweighteddirectedgraph.code(N, a, b, c)
    assert actual == expected


@parameterized.expand(
    [
        (
            wd_K4,
            1,
            [INF, 0, 1, 2, 4]
        ),
        (
            wd_sparse_graph,
            2,
            [INF, 54, 0, 2, 5, 9, 14, 20, 27, 35, 44]
        ),
        (
            w_no_edge_graph,
            3,
            [INF, INF, INF, 0]
        ),
        (
            wd_negative_weight_graph,
            1,
            [INF, 0, 3, 1]
        )
    ]
)
def test_bellman_ford(G, s, expected):
    sssp = bellman_ford.code(INF)
    actual = sssp(G, s)
    assert actual == expected


@parameterized.expand(
    [
        (
            wd_K4,
            1,
            [INF, 0, 1, 2, 4]
        ),
        (
            wd_sparse_graph,
            2,
            [INF, 54, 0, 2, 5, 9, 14, 20, 27, 35, 44]
        ),
        (
            w_no_edge_graph,
            3,
            [INF, INF, INF, 0]
        ),
        (
            wd_zero_weight_graph,
            1,
            [INF, 0, 0, 0]
        )
    ]
)
def test_dijkstra(G, s, expected):
    sssp = dijkstra.code(INF)
    actual = sssp(G, s)
    assert actual == expected


@parameterized.expand(
    [
        (
            wd_K4,
            4
        ),
        (
            wd_sparse_graph,
            45
        ),
        (
            wd_zero_weight_graph,
            0
        )
    ]
)
def test_prim(G, expected):
    mcst = prim.code()
    actual = mcst(G)
    assert actual == expected


@parameterized.expand(
    [
        (
            wd_K4,
            [
                [0, INF, INF, INF, INF],
                [INF, 0, 1, 2, 4],
                [INF, 1, 0, 1, 3],
                [INF, 2, 1, 0, 2],
                [INF, 4, 3, 2, 0]
            ]
        ),
        (
            wd_sparse_graph,
            [
                [0, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
                [INF, 0, 1, 3, 6, 10, 15, 21, 28, 36, 45],
                [INF, 54, 0, 2, 5, 9, 14, 20, 27, 35, 44],
                [INF, 52, 53, 0, 3, 7, 12, 18, 25, 33, 42],
                [INF, 49, 50, 52, 0, 4, 9, 15, 22, 30, 39],
                [INF, 45, 46, 48, 51, 0, 5, 11, 18, 26, 35],
                [INF, 40, 41, 43, 46, 50, 0, 6, 13, 21, 30],
                [INF, 34, 35, 37, 40, 44, 49, 0, 7, 15, 24],
                [INF, 27, 28, 30, 33, 37, 42, 48, 0, 8, 17],
                [INF, 19, 20, 22, 25, 29, 34, 40, 47, 0, 9],
                [INF, 10, 11, 13, 16, 20, 25, 31, 38, 46, 0]
            ]
        ),
        (
            w_no_edge_graph,
            [
                [0, INF, INF, INF],
                [INF, 0, INF, INF],
                [INF, INF, 0, INF],
                [INF, INF, INF, 0]
            ]
        ),
        (
            wd_negative_weight_graph,
            [
                [0, INF, INF, INF],
                [INF, 0, 3, 1],
                [INF, 0, 0, -2],
                [INF, 2, 4, 0]
            ]
        )
    ]
)
def test_warshall_floyd(G, expected):
    apsp = warshall_floyd.code(INF)
    actual = apsp(G)
    assert actual == expected


@parameterized.expand(
    [
        (
            dag_line,
            [
                [],
                [2, 4, 5],
                [],
                [1, 2, 4, 5],
                [2, 5],
                [2]
            ]
        ),
        (
            dag_binary_tree,
            [
                [],
                [4, 5, 6, 8],
                [1, 3, 4, 5, 6, 7],
                [],
                [3],
                [],
                [],
                [],
                [5, 6]
            ]
        ),
        (
            dag_star,
            [
                [],
                [2, 3, 4, 5],
                [],
                [],
                []
            ]
        ),
        (
            dag_grid,
            [
                [],
                [2, 3, 4, 5, 6, 7, 8, 9],
                [3, 5, 6, 8, 9],
                [6, 9],
                [5, 6, 7, 8, 9],
                [6, 8, 9],
                [9],
                [8, 9],
                [9],
                []
            ]
        ),
        (
            no_edge_graph,
            [
                [],
                [],
                [],
                [],
                []
            ]
        )
    ]
)
def test_topological_sort(G, expected):
    ts = topological_sort.code()
    actual = ts(G)
    assert all(
        actual.index(i) < actual.index(v)
        for i, V in enumerate(expected[1:], start=1)
        for v in V
    )
