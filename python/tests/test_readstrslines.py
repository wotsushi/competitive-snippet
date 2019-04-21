import unittest
from snippets import readstrslines


class TestReadStrsLines(unittest.TestCase):
    def test_three_pairs(self):
        N = 3
        str_mat = iter([
            'wotsushi PYTHON',
            '1!2@3# foo',
            'Wo2_shi! AtCoder'
        ])
        S, T = readstrslines.code(lambda: next(str_mat), N)
        self.assertEqual(S, ('wotsushi', '1!2@3#', 'Wo2_shi!'))
        self.assertEqual(T, ('PYTHON', 'foo', 'AtCoder'))

    def test_one_pair(self):
        N = 1
        str_mat = iter(['wotsushi PYTHON'])
        S, T = readstrslines.code(lambda: next(str_mat), N)
        self.assertEqual(S, ('wotsushi',))
        self.assertEqual(T, ('PYTHON',))

    def test_no_pair(self):
        N = 0
        str_mat = iter([])
        S, T = readstrslines.code(lambda: next(str_mat), N)
        self.assertEqual(S, ())
        self.assertEqual(T, ())
