def code(MOD):
    class ModInt:
        def __init__(self, x):
            self.x = x % MOD

        def __str__(self):
            return str(self.x)

        __repr__ = __str__

        def __add__(self, other):
            return (
                ModInt(self.x + other.x) if isinstance(other, ModInt) else
                ModInt(self.x + other)
            )

        def __sub__(self, other):
            return (
                ModInt(self.x - other.x) if isinstance(other, ModInt) else
                ModInt(self.x - other)
            )

        def __mul__(self, other):
            return (
                ModInt(self.x * other.x) if isinstance(other, ModInt) else
                ModInt(self.x * other)
            )

        def __truediv__(self, other):
            return (
                ModInt(
                    self.x * pow(other.x, MOD - 2, MOD)
                ) if isinstance(other, ModInt) else
                ModInt(self.x * pow(other, MOD - 2, MOD))
            )

        def __pow__(self, other):
            return (
                ModInt(
                    pow(self.x, other.x, MOD)
                ) if isinstance(other, ModInt) else
                ModInt(pow(self.x, other, MOD))
            )

        def __radd__(self, other):
            return ModInt(other + self.x)

        def __rsub__(self, other):
            return ModInt(other - self.x)

        def __rmul__(self, other):
            return ModInt(other * self.x)

        def __rtruediv__(self, other):
            return ModInt(other * pow(self.x, MOD - 2, MOD))

        def __rpow__(self, other):
            return ModInt(pow(other, self.x, MOD))

    return ModInt
