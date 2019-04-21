import unittest
from snippets import readstrandintlines


class TestReadStrAndIntLines(unittest.TestCase):
    def test_three_pairs(self):
        N = 3
        lines = iter(['wotsushi 1', 'PYTHON 2', 'Wo2_shi! 3'])
        S, A = readstrandintlines.code(lambda: next(lines), N)
        self.assertEqual(S, ('wotsushi', 'PYTHON', 'Wo2_shi!'))
        self.assertEqual(A, (1, 2, 3))

    def test_single_pair(self):
        N = 1
        lines = iter(['...@..#+. 0'])
        S, A = readstrandintlines.code(lambda: next(lines), N)
        self.assertEqual(S, ('...@..#+.',))
        self.assertEqual(A, (0,))

    def test_no_pair(self):
        N = 0
        lines = iter([])
        S, A = readstrandintlines.code(lambda: next(lines), N)
        self.assertEqual(S, ())
        self.assertEqual(A, ())
