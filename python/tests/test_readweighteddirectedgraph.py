import unittest
from snippets import readweighteddirectedgraph


class TestReadWeightedDirectedGraph(unittest.TestCase):
    def test_complete_graph(self):
        G = readweighteddirectedgraph.code(
            3,
            [1, 1, 2, 2, 3, 3],
            [2, 3, 1, 3, 1, 2],
            [1, 1, 2, 3, 5, 8])
        self.assertEqual(
            G,
            [
                {},
                {
                    2: 1,
                    3: 1
                },
                {
                    1: 2,
                    3: 3
                },
                {
                    1: 5,
                    2: 8
                }
            ]
        )

    def test_sprase_graph(self):
        G = readweighteddirectedgraph.code(
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
                    7: 4,
                    8: 4
                },
                {},
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
                {},
                {},
                {},
                {}
            ]
        )

    def test_no_edge(self):
        G = readweighteddirectedgraph.code(3, [], [], [])
        self.assertEqual(
            G,
            [
                {},
                {},
                {},
                {}
            ]
        )
