import unittest
from snippets import readweightedgraph


class TestReadWeightedGraph(unittest.TestCase):
    def test_complete_graph(self):
        G = readweightedgraph.code(
            4,
            [1, 2, 3, 1, 2, 1],
            [2, 3, 4, 3, 4, 4],
            [1, 1, 2, 3, 5, 8]
        )
        self.assertEqual(
            G,
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
            ]
        )

    def test_sprase_graph(self):
        G = readweightedgraph.code(
            10,
            [3, 1, 4, 1, 5],
            [2, 7, 1, 8, 2],
            [1, 4, 1, 4, 2]
        )
        self.assertEqual(
            G,
            [
                {},
                {
                    4: 1,
                    7: 4,
                    8: 4
                },
                {
                    3: 1,
                    5: 2
                },
                {
                    2: 1
                },
                {
                    1: 1
                },
                {
                    2: 2
                },
                {},
                {
                    1: 4
                },
                {
                    1: 4
                },
                {},
                {}
            ]
        )

    def test_no_edge(self):
        G = readweightedgraph.code(3, [], [], [])
        self.assertEqual(
            G,
            [
                {},
                {},
                {},
                {}
            ]
        )
