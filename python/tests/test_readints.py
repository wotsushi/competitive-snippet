import unittest
from snippets import readints


class TestReadInts(unittest.TestCase):
    def test_two_positive(self):
        res = readints.code(lambda: '1 2')
        self.assertEqual(res, (1, 2))

    def test_zero_and_negative(self):
        res = readints.code(lambda: '0 -1')
        self.assertEqual(res, (0, -1))

    def test_same_ints(self):
        res = readints.code(lambda: '3 3')
        self.assertEqual(res, (3, 3))
