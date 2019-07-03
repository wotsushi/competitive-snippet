from snippets.datastructure import modint
from itertools import accumulate
ModInt = modint.code(10**9 + 7)


def code(_N):
    fact = list(
        accumulate(
            [ModInt(1)] + list(range(1, _N + 1)),
            lambda acc, i: acc * i
        )
    )

    def comb(n, r):
        return fact[n] / (fact[r] * fact[n - r])
    return comb
