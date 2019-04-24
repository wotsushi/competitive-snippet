import unittest
from snippets import readdirectedgraph


class TestReadDirectedGraph(unittest.TestCase):
    def test_complete_graph(self):
        G = readdirectedgraph.code(3, [1, 1, 2, 2, 3, 3], [2, 3, 1, 3, 1, 2])
        self.assertEqual(
            G,
            [
                set(),
                {2, 3},
                {1, 3},
                {1, 2}
            ])

    def test_sprase_graph(self):
        G = readdirectedgraph.code(10, [3, 1, 4, 1, 5], [2, 7, 1, 8, 2])
        self.assertEqual(
            G,
            [
                set(),
                {7, 8},
                set(),
                {2},
                {1},
                {2},
                set(),
                set(),
                set(),
                set(),
                set()
            ]
        )

    def test_no_edge(self):
        G = readdirectedgraph.code(3, [], [])
        self.assertEqual(
            G,
            [
                set(),
                set(),
                set(),
                set()
            ]
        )
