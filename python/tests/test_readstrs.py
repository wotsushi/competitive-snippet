import unittest
from snippets import readstrs


class Test(unittest.TestCase):
    def test_two_ascii_lowercase(self):
        S, T = readstrs.code(lambda: 'wotsushi python')
        self.assertEqual(S, 'wotsushi')
        self.assertEqual(T, 'python')

    def test_two_ascii_uppercase(self):
        S, T = readstrs.code(lambda: 'WOTSUSHI PYTHON')
        self.assertEqual(S, 'WOTSUSHI')
        self.assertEqual(T, 'PYTHON')

    def test_two_digit_strs(self):
        S, T = readstrs.code(lambda: '31415 2718')
        self.assertEqual(S, '31415')
        self.assertEqual(T, '2718')

    def test_two_symbol_strs(self):
        S, T = readstrs.code(lambda: '...@..#+. .........')
        self.assertEqual(S, '...@..#+.')
        self.assertEqual(T, '.........')

    def test_mix(self):
        S, T = readstrs.code(lambda: 'Wo2_shi! pYtHoN')
        self.assertEqual(S, 'Wo2_shi!')
        self.assertEqual(T, 'pYtHoN')
