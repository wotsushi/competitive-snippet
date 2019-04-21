import unittest
from snippets import readintandstrlines


class TestReadIntAndStrLines(unittest.TestCase):
    def test_three_pairs(self):
        N = 3
        lines = iter(['1 wotsushi', '2 PYTHON', '3 Wo2_shi!'])
        A, S = readintandstrlines.code(lambda: next(lines), N)
        self.assertEqual(A, (1, 2, 3))
        self.assertEqual(S, ('wotsushi', 'PYTHON', 'Wo2_shi!'))

    def test_single_pair(self):
        N = 1
        lines = iter(['0 ...@..#+.'])
        A, S = readintandstrlines.code(lambda: next(lines), N)
        self.assertEqual(A, (0,))
        self.assertEqual(S, ('...@..#+.',))

    def test_no_pair(self):
        N = 0
        lines = iter([])
        A, S = readintandstrlines.code(lambda: next(lines), N)
        self.assertEqual(A, ())
        self.assertEqual(S, ())
