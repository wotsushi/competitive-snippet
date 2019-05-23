import unittest
from snippets import union_find_tree


class TestUnionFindTree(unittest.TestCase):
    def test_all_same(self):
        UnionFindTree = union_find_tree.code()
        uft = UnionFindTree(5)
        uft.union(1, 2)
        uft.union(2, 3)
        uft.union(4, 5)
        uft.union(5, 1)
        self.assertTrue(uft.find(1) == uft.find(2))
        self.assertTrue(uft.find(2) == uft.find(3))
        self.assertTrue(uft.find(3) == uft.find(4))
        self.assertTrue(uft.find(4) == uft.find(5))
        self.assertTrue(uft.same(3, 1))
        self.assertTrue(uft.same(4, 2))
        self.assertTrue(uft.same(1, 5))

    def test_independent(self):
        UnionFindTree = union_find_tree.code()
        uft = UnionFindTree(3)
        self.assertTrue(uft.find(1) == 1)
        self.assertTrue(uft.find(2) == 2)
        self.assertTrue(uft.find(3) == 3)
        self.assertFalse(uft.same(3, 1))
        self.assertFalse(uft.same(2, 3))
        self.assertFalse(uft.same(1, 2))

    def test_two_group(self):
        UnionFindTree = union_find_tree.code()
        uft = UnionFindTree(5)
        uft.union(1, 3)
        uft.union(2, 4)
        uft.union(5, 3)
        self.assertTrue(uft.find(1) == uft.find(3))
        self.assertTrue(uft.find(3) == uft.find(5))
        self.assertTrue(uft.find(2) == uft.find(4))
        self.assertFalse(uft.find(1) == uft.find(2))
        self.assertTrue(uft.same(1, 3))
        self.assertTrue(uft.same(2, 4))
        self.assertTrue(uft.same(3, 5))
        self.assertFalse(uft.same(1, 2))
        self.assertFalse(uft.same(2, 3))
        self.assertFalse(uft.same(3, 4))
        self.assertFalse(uft.same(4, 5))
