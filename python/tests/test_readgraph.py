import unittest
from snippets import readgraph


class TestReadGraph(unittest.TestCase):
    def test_complete_graph(self):
        G = readgraph.code(4, [1, 2, 3, 1, 2, 1], [2, 3, 4, 3, 4, 4])
        self.assertEqual(
            G,
            [
                set(),
                {2, 3, 4},
                {1, 3, 4},
                {1, 2, 4},
                {1, 2, 3}
            ])

    def test_sprase_graph(self):
        G = readgraph.code(10, [3, 1, 4, 1, 5], [2, 7, 1, 8, 2])
        self.assertEqual(
            G,
            [
                set(),
                {4, 7, 8},
                {3, 5},
                {2},
                {1},
                {2},
                set(),
                {1},
                {1},
                set(),
                set()
            ]
        )

    def test_no_edge(self):
        G = readgraph.code(3, [], [])
        self.assertEqual(
            G,
            [
                set(),
                set(),
                set(),
                set()
            ]
        )
