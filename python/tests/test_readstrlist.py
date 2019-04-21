import unittest
from snippets import readstrlist


class TestReadStrList(unittest.TestCase):
    def test_three_strs(self):
        S = readstrlist.code(lambda: 'wotsushi PYTHON Wo2_shi!')
        self.assertEqual(S, ['wotsushi', 'PYTHON', 'Wo2_shi!'])

    def test_single_str(self):
        S = readstrlist.code(lambda: '...@..#+.')
        self.assertEqual(S, ['...@..#+.'])

    def test_no_str(self):
        S = readstrlist.code(lambda: '')
        self.assertEqual(S, [])
