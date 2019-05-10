import unittest
from snippets import segment_tree
from operator import add


class TestSegmentTree(unittest.TestCase):
    def test_rmq(self):
        SegmentTree = segment_tree.code()
        rmq = SegmentTree(8, min, 10**18)
        for i, x in enumerate([5, 3, 7, 9, 6, 4, 1, 2], start=1):
            rmq[i] = x
        self.assertEqual(rmq[1:9], 1)
        self.assertEqual(rmq[1:4], 3)
        self.assertEqual(rmq[4:6], 6)
        self.assertEqual(rmq[3:4], 7)
        rmq[4] = 0
        self.assertEqual(rmq[1:9], 0)
        self.assertEqual(rmq[1:4], 3)
        self.assertEqual(rmq[4:6], 0)
        self.assertEqual(rmq[3:4], 7)

    def test_bit(self):
        SegmentTree = segment_tree.code()
        bit = SegmentTree(8, add, 0)
        for i, x in enumerate([5, 3, 7, 9, 6, 4, 1, 2], start=1):
            bit[i] = x
        self.assertEqual(bit[1:2], 5)
        self.assertEqual(bit[1:3], 8)
        self.assertEqual(bit[1:4], 15)
        self.assertEqual(bit[1:5], 24)
        self.assertEqual(bit[1:9], 37)
        bit[4] = bit[4:5] + 1
        self.assertEqual(bit[1:2], 5)
        self.assertEqual(bit[1:3], 8)
        self.assertEqual(bit[1:4], 15)
        self.assertEqual(bit[1:5], 25)
        self.assertEqual(bit[1:9], 38)

    def test_not_pow_of_two(self):
        SegmentTree = segment_tree.code()
        rmq = SegmentTree(3, min, 10**18)
        for i, x in enumerate([5, 3, 7], start=1):
            rmq[i] = x
        self.assertEqual(rmq[1:2], 5)
        self.assertEqual(rmq[1:3], 3)
        self.assertEqual(rmq[1:4], 3)
        self.assertEqual(rmq[2:3], 3)
        self.assertEqual(rmq[2:4], 3)
        self.assertEqual(rmq[3:4], 7)
        rmq[2] = 6
        rmq[3] = 4
        self.assertEqual(rmq[1:2], 5)
        self.assertEqual(rmq[1:3], 5)
        self.assertEqual(rmq[1:4], 4)
        self.assertEqual(rmq[2:3], 6)
        self.assertEqual(rmq[2:4], 4)
        self.assertEqual(rmq[3:4], 4)
