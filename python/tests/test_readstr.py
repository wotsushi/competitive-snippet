import unittest
from snippets import readstr


class Test(unittest.TestCase):
    def test_only_ascii_lowercase(self):
        self.assertEqual(readstr.code(lambda: 'wotsushi'), 'wotsushi')

    def test_only_ascii_uppercase(self):
        self.assertEqual(readstr.code(lambda: 'WOTSUSHI'), 'WOTSUSHI')

    def test_only_digits(self):
        self.assertEqual(readstr.code(lambda: '31415'), '31415')

    def test_only_symbols(self):
        self.assertEqual(readstr.code(lambda: '...@..#+.'), '...@..#+.')

    def test_white_space(self):
        self.assertEqual(readstr.code(lambda: 'wo tsu shi'), 'wo tsu shi')

    def test_mix(self):
        self.assertEqual(readstr.code(lambda: 'Wo 2_shi!'), 'Wo 2_shi!')
