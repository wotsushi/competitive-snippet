import unittest
from snippets import prim


class TestPrim(unittest.TestCase):
    def test_complete_graph(self):
        mcst = prim.code()
        res = mcst(
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
        self.assertEqual(
            res,
            4
        )

    def test_sprase_graph(self):
        mcst = prim.code()
        res = mcst(
            [
                {},
                {
                    2: 1,
                    10: 10
                },
                {
                    1: 1,
                    3: 2
                },
                {
                    2: 2,
                    4: 3
                },
                {
                    3: 3,
                    5: 4
                },
                {
                    4: 4,
                    6: 5
                },
                {
                    5: 5,
                    7: 6
                },
                {
                    6: 6,
                    8: 7
                },
                {
                    7: 7,
                    9: 8
                },
                {
                    8: 8,
                    10: 9
                },
                {
                    9: 9,
                    1: 10
                }
            ]
        )
        self.assertEqual(
            res,
            45
        )

    def test_zero_weight(self):
        mcst = prim.code()
        res = mcst(
            [
                {},
                {
                    2: 0,
                    3: 0
                },
                {
                    1: 0,
                    3: 0
                },
                {
                    1: 0,
                    2: 0
                }
            ]
        )
        self.assertEqual(
            res,
            0
        )

    def test_negative_weight(self):
        mcst = prim.code()
        res = mcst(
            [
                {},
                {
                    2: -1,
                    3: 0
                },
                {
                    1: -1,
                    3: -1
                },
                {
                    1: 0,
                    2: -1
                }
            ]
        )
        self.assertEqual(
            res,
            -2
        )
