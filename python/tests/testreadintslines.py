import unittest
from snippet import readintslines


class TestReadIntsLines(unittest.TestCase):
    def test_three_pairs(self):
        N = 3
        int_mat = (f'{i} {-i}' for i in range(1, N + 1))
        A, B = readintslines.code(lambda: next(int_mat), N)
        self.assertEqual(A, (1, 2, 3))
        self.assertEqual(B, (-1, -2, -3))

    def test_one_pair(self):
        N = 1
        int_mat = (f'0 0' for _ in range(1, N + 1))
        A, B = readintslines.code(lambda: next(int_mat), N)
        self.assertEqual(A, (0,))
        self.assertEqual(B, (0,))

    def test_no_pair(self):
        N = 0
        int_mat = ()
        A, B = readintslines.code(lambda: next(int_mat), N)
        self.assertEqual(A, ())
        self.assertEqual(B, ())
