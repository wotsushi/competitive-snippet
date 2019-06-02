import unittest
from snippets import modint


class TestModInt(unittest.TestCase):
    def test_str(self):
        ModInt = modint.code(10**9 + 7)
        N = ModInt(10**9 + 8)
        self.assertEqual(str(N), '1')

    def test_repr(self):
        ModInt = modint.code(10**9 + 7)
        N = ModInt(10**9 + 8)
        self.assertEqual(repr(N), '1')

    def test_add_int(self):
        ModInt = modint.code(10**9 + 7)
        A = ModInt(10**9 + 8)
        B = 1
        self.assertEqual((A + B).x, 2)

    def test_add_modint(self):
        ModInt = modint.code(10**9 + 7)
        A = ModInt(10**9 + 8)
        B = ModInt(1)
        self.assertEqual((A + B).x, 2)

    def test_sub_int(self):
        ModInt = modint.code(10**9 + 7)
        A = ModInt(10**9 + 8)
        B = 1
        self.assertEqual((A - B).x, 0)

    def test_sub_modint(self):
        ModInt = modint.code(10**9 + 7)
        A = ModInt(10**9 + 8)
        B = ModInt(1)
        self.assertEqual((A - B).x, 0)

    def test_mul_int(self):
        ModInt = modint.code(10**9 + 7)
        A = ModInt(10**9 + 8)
        B = 2
        self.assertEqual((A * B).x, 2)

    def test_mul_modint(self):
        ModInt = modint.code(10**9 + 7)
        A = ModInt(10**9 + 8)
        B = ModInt(2)
        self.assertEqual((A * B).x, 2)

    def test_div_int(self):
        ModInt = modint.code(10**9 + 7)
        A = ModInt(10**9 + 8)
        B = 2
        self.assertEqual((A / B).x, 500000004)

    def test_div_modint(self):
        ModInt = modint.code(10**9 + 7)
        A = ModInt(10**9 + 8)
        B = ModInt(2)
        self.assertEqual((A / B).x, 500000004)

    def test_pow_int(self):
        ModInt = modint.code(10**9 + 7)
        A = ModInt(10**9 + 9)
        B = 3
        self.assertEqual((A**B).x, 8)

    def test_pow_modint(self):
        ModInt = modint.code(10**9 + 7)
        A = ModInt(10**9 + 9)
        B = ModInt(3)
        self.assertEqual((A**B).x, 8)

    def test_radd(self):
        ModInt = modint.code(10**9 + 7)
        A = 1
        B = ModInt(10**9 + 8)
        self.assertEqual((A + B).x, 2)

    def test_rsub(self):
        ModInt = modint.code(10**9 + 7)
        A = 1
        B = ModInt(10**9 + 8)
        self.assertEqual((A - B).x, 0)

    def test_rmul(self):
        ModInt = modint.code(10**9 + 7)
        A = 2
        B = ModInt(10**9 + 8)
        self.assertEqual((A * B).x, 2)

    def test_rdiv(self):
        ModInt = modint.code(10**9 + 7)
        A = 1
        B = ModInt(10**9 + 9)
        self.assertEqual((A / B).x, 500000004)

    def test_rpow(self):
        ModInt = modint.code(10**9 + 7)
        A = 2
        B = ModInt(10**9 + 10)
        self.assertEqual((A**B).x, 8)
