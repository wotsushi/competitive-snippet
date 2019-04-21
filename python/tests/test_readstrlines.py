import unittest
from snippets import readstrlines


class TestReadStrLines(unittest.TestCase):
    def test_three_strs(self):
        N = 3
        strs = iter(['wotsushi', 'PYTHON', 'Wo2_shi!'])
        A = readstrlines.code(lambda: next(strs), N)
        self.assertEqual(A, ['wotsushi', 'PYTHON', 'Wo2_shi!'])

    def test_single_str(self):
        N = 1
        strs = iter(['...@..#+. .........'])
        A = readstrlines.code(lambda: next(strs), N)
        self.assertEqual(A, ['...@..#+. .........'])

    def test_no_str(self):
        N = 0
        strs = iter([])
        A = readstrlines.code(lambda: next(strs), N)
        self.assertEqual(A, [])
