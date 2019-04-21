import unittest
from snippets import readints


class TestReadInts(unittest.TestCase):
    def test_two_positive(self):
        N, M = readints.code(lambda: '1 2')
        self.assertEqual(N, 1)
        self.assertEqual(M, 2)

    def test_zero_and_negative(self):
        N, M = readints.code(lambda: '0 -1')
        self.assertEqual(N, 0)
        self.assertEqual(M, -1)

    def test_same_ints(self):
        N, M = readints.code(lambda: '3 3')
        self.assertEqual(N, 3)
        self.assertEqual(M, 3)
