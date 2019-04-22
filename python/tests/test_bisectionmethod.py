import unittest
from snippets import bisectionmethod


class TestBisectionMethod(unittest.TestCase):
    def test_findmax(self):
        bis = bisectionmethod.code()
        opt = bis(lambda n: n**3 < 30, 0, 10**18)
        self.assertEqual(opt, 3)

    def test_findmin(self):
        bis = bisectionmethod.code()
        opt = bis(lambda n: n**3 > 30, 10**18, 0)
        self.assertEqual(opt, 4)

    def test_ok_is_max(self):
        bis = bisectionmethod.code()
        opt = bis(lambda n: n**3 < 30, 3, 10**18)
        self.assertEqual(opt, 3)

    def test_ok_is_min(self):
        bis = bisectionmethod.code()
        opt = bis(lambda n: n**3 > 30, 4, 0)
        self.assertEqual(opt, 4)

    def test_singleton(self):
        bis = bisectionmethod.code()
        opt = bis(lambda n: n**3 < 30, 3, 4)
        self.assertEqual(opt, 3)
