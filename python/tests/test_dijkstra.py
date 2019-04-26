import unittest
from snippets import dijkstra


class TestDijkstra(unittest.TestCase):
    def test_complete_graph(self):
        INF = 10**3
        sssp = dijkstra.code(INF)
        dp = sssp(
            [
                {},
                {
                    2: 1,
                    3: 3,
                    4: 8
                },
                {
                    1: 1,
                    3: 1,
                    4: 5
                },
                {
                    1: 3,
                    2: 1,
                    4: 2
                },
                {
                    1: 8,
                    2: 5,
                    3: 2
                }
            ],
            1
        )
        self.assertEqual(
            dp,
            [
                INF,
                0,
                1,
                2,
                4
            ]
        )

    def test_sprase_graph(self):
        INF = 10**3
        sssp = dijkstra.code(INF)
        dp = sssp(
            [
                {},
                {
                    2: 1
                },
                {
                    3: 2
                },
                {
                    4: 3
                },
                {
                    5: 4
                },
                {
                    6: 5
                },
                {
                    7: 6
                },
                {
                    8: 7
                },
                {
                    9: 8
                },
                {
                    10: 9
                },
                {
                    1: 10
                }
            ],
            2
        )
        self.assertEqual(
            dp,
            [
                INF,
                54,
                0,
                2,
                5,
                9,
                14,
                20,
                27,
                35,
                44
            ]
        )

    def test_no_edge(self):
        INF = 10**3
        sssp = dijkstra.code(INF)
        dp = sssp(
            [
                {},
                {},
                {},
                {}
            ],
            3
        )
        self.assertEqual(
            dp,
            [
                INF,
                INF,
                INF,
                0
            ]
        )

    def test_zero_weight(self):
        INF = 10**3
        sssp = dijkstra.code(INF)
        dp = sssp(
            [
                {},
                {
                    2: 0,
                    3: 1,
                },
                {
                    3: 0
                },
                {}
            ],
            1
        )
        self.assertEqual(
            dp,
            [
                INF,
                0,
                0,
                0
            ]
        )
