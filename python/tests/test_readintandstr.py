import unittest
from snippets import readintandstr


class TestReadIntAndStr(unittest.TestCase):
    def test_positive_and_lowercase(self):
        N, S = readintandstr.code(lambda: '1 wotsushi')
        self.assertEqual(N, 1)
        self.assertEqual(S, 'wotsushi')

    def test_zero_and_only_symbols(self):
        N, S = readintandstr.code(lambda: '0 ...@..#+.')
        self.assertEqual(N, 0)
        self.assertEqual(S, '...@..#+.')

    def test_negative(self):
        N, S = readintandstr.code(lambda: '-1 Wo2_shi!')
        self.assertEqual(N, -1)
        self.assertEqual(S, 'Wo2_shi!')
