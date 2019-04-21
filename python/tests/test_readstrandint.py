import unittest
from snippets import readstrandint


class TestReadStrAndInt(unittest.TestCase):
    def test_lowercase_and_positive(self):
        S, N = readstrandint.code(lambda: 'wotsushi 1')
        self.assertEqual(S, 'wotsushi')
        self.assertEqual(N, 1)

    def test_only_symbols_and_zero(self):
        S, N = readstrandint.code(lambda: '...@..#+. 0')
        self.assertEqual(S, '...@..#+.')
        self.assertEqual(N, 0)

    def test_negative(self):
        S, N = readstrandint.code(lambda: 'Wo2_shi! -1')
        self.assertEqual(S, 'Wo2_shi!')
        self.assertEqual(N, -1)
