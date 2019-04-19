import unittest
from snippets import readint


class TestReadInt(unittest.TestCase):
    def test_positive(self):
        res = readint.code(lambda: '1')
        self.assertEqual(res, 1)

    def test_zero(self):
        res = readint.code(lambda: '0')
        self.assertEqual(res, 0)

    def test_negative(self):
        res = readint.code(lambda: '-1')
        self.assertEqual(res, -1)
