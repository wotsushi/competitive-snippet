import unittest
from snippets import readstr


class Test(unittest.TestCase):
    def test_only_ascii_lowercase(self):
        S = readstr.code(lambda: 'wotsushi')
        self.assertEqual(S, 'wotsushi')

    def test_only_ascii_uppercase(self):
        S = readstr.code(lambda: 'WOTSUSHI')
        self.assertEqual(S, 'WOTSUSHI')

    def test_only_digits(self):
        S = readstr.code(lambda: '31415')
        self.assertEqual(S, '31415')

    def test_only_symbols(self):
        S = readstr.code(lambda: '...@..#+.')
        self.assertEqual(S, '...@..#+.')

    def test_white_space(self):
        S = readstr.code(lambda: 'wo tsu shi')
        self.assertEqual(S, 'wo tsu shi')

    def test_mix(self):
        S = readstr.code(lambda: 'Wo 2_shi!')
        self.assertEqual(S, 'Wo 2_shi!')
