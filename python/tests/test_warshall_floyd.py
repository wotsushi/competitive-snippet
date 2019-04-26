import unittest
from snippets import warshall_floyd


class TestWarshallFloyd(unittest.TestCase):
    def test_complete_graph(self):
        INF = 10**3
        apsp = warshall_floyd.code(INF)
        dp = apsp(
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
            dp,
            [
                [
                    0,
                    INF,
                    INF,
                    INF,
                    INF
                ],
                [
                    INF,
                    0,
                    1,
                    2,
                    4
                ],
                [
                    INF,
                    1,
                    0,
                    1,
                    3
                ],
                [
                    INF,
                    2,
                    1,
                    0,
                    2
                ],
                [
                    INF,
                    4,
                    3,
                    2,
                    0
                ]
            ]
        )

    def test_sprase_graph(self):
        INF = 10**3
        apsp = warshall_floyd.code(INF)
        dp = apsp(
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
                    1: 4
                }
            ],
        )
        self.assertEqual(
            dp,
            [
                [
                    0,
                    INF,
                    INF,
                    INF,
                    INF
                ],
                [
                    INF,
                    0,
                    1,
                    3,
                    6
                ],
                [
                    INF,
                    9,
                    0,
                    2,
                    5
                ],
                [
                    INF,
                    7,
                    8,
                    0,
                    3
                ],
                [
                    INF,
                    4,
                    5,
                    7,
                    0
                ],
            ]
        )

    def test_no_edge(self):
        INF = 10**3
        apsp = warshall_floyd.code(INF)
        dp = apsp(
            [
                {},
                {},
                {}
            ]
        )
        self.assertEqual(
            dp,
            [
                [
                    0,
                    INF,
                    INF
                ],
                [
                    INF,
                    0,
                    INF
                ],
                [
                    INF,
                    INF,
                    0
                ]
            ]
        )

    def test_non_positive_weight(self):
        INF = 10**3
        apsp = warshall_floyd.code(INF)
        dp = apsp(
            [
                {},
                {
                    2: 1,
                    3: 2
                },
                {
                    3: 0
                },
                {
                    1: -1,
                }
            ],
        )
        self.assertEqual(
            dp,
            [
                [
                    0,
                    INF,
                    INF,
                    INF
                ],
                [
                    INF,
                    0,
                    1,
                    1
                ],
                [
                    INF,
                    -1,
                    0,
                    0
                ],
                [
                    INF,
                    -1,
                    0,
                    0
                ]
            ]
        )
