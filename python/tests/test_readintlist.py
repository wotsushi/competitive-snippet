import unittest
from snippet import readintlist


class TestReadIntList(unittest.TestCase):
    def test_three_ints(self):
        A = readintlist.code(lambda: '1 2 3')
        self.assertEqual(A, [1, 2, 3])

    def test_single_int(self):
        A = readintlist.code(lambda: '-1')
        self.assertEqual(A, [-1])

    def test_no_int(self):
        A = readintlist.code(lambda: '')
        self.assertEqual(A, [])
