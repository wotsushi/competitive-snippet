import unittest
from snippet import readintlines


class TestReadIntLines(unittest.TestCase):
    def test_three_ints(self):
        N = 3
        ints = map(str, range(1, N + 1))
        A = readintlines.code(lambda: next(ints), N)
        self.assertEqual(A, [1, 2, 3])

    def test_single_int(self):
        N = 1
        ints = map(str, [-1])
        A = readintlines.code(lambda: next(ints), N)
        self.assertEqual(A, [-1])

    def test_no_int(self):
        N = 0
        ints = map(str, range(0))
        A = readintlines.code(lambda: next(ints), N)
        self.assertEqual(A, [])
