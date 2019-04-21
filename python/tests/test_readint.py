import unittest
from snippets import readint


class TestReadInt(unittest.TestCase):
    def test_positive(self):
        N = readint.code(lambda: '1')
        self.assertEqual(N, 1)

    def test_zero(self):
        N = readint.code(lambda: '0')
        self.assertEqual(N, 0)

    def test_negative(self):
        N = readint.code(lambda: '-1')
        self.assertEqual(N, -1)
