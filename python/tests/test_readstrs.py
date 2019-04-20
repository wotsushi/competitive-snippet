import unittest
from snippets import readstrs


class Test(unittest.TestCase):
    def test_two_ascii_lowercase(self):
        self.assertEqual(
            readstrs.code(lambda: 'wotsushi python'),
            ('wotsushi', 'python')
        )

    def test_two_ascii_uppercase(self):
        self.assertEqual(
            readstrs.code(lambda: 'WOTSUSHI PYTHON'),
            ('WOTSUSHI', 'PYTHON')
        )

    def test_two_digit_strs(self):
        self.assertEqual(
            readstrs.code(lambda: '31415 2718'),
            ('31415', '2718')
        )

    def test_two_symbol_strs(self):
        self.assertEqual(
            readstrs.code(lambda: '...@..#+. .........'),
            ('...@..#+.', '.........')
        )

    def test_mix(self):
        self.assertEqual(
            readstrs.code(lambda: 'Wo2_shi! pYtHoN'),
            ('Wo2_shi!', 'pYtHoN')
        )
