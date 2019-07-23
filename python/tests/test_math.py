from snippets.math import intceil, combination, eratosthenes_sieve
from parameterized import parameterized


@parameterized.expand(
    [
        (-11, 10, -1),
        (-10, 10, -1),
        (-9, 10, 0),
        (-1, 10, 0),
        (0, 10, 0),
        (1, 10, 1),
        (9, 10, 1),
        (10, 10, 1),
        (11, 10, 2),
        (-1, 1, -1),
        (0, 1, 0),
        (1, 1, 1),
        (314159265358979323845999999, 314159265358979323846, 10**6),
        (314159265358979323846000000, 314159265358979323846, 10**6),
        (314159265358979323846000001, 314159265358979323846, 10**6 + 1)
    ]
)
def test_intceil(a, b, expected):
    iceil = intceil.code()
    actual = iceil(a, b)
    assert actual == expected


@parameterized.expand(
    [
        (0, 0, 1),
        (1, 0, 1),
        (1, 1, 1),
        (2, 0, 1),
        (2, 1, 2),
        (2, 2, 1),
        (3, 0, 1),
        (3, 1, 3),
        (3, 2, 3),
        (3, 3, 1),
        (4, 0, 1),
        (4, 1, 4),
        (4, 2, 6),
        (4, 3, 4),
        (4, 4, 1),
        (100000, 50000, 149033233),
        (31415, 27182, 181880515)
    ]
)
def test_comb(n, r, expected):
    comb = combination.code(n)
    actual = comb(n, r).x
    assert actual == expected


primes = eratosthenes_sieve.code(10**6)


@parameterized.expand(
    [
        (0, False),
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (5, True),
        (6, False),
        (7, True),
        (8, False),
        (9, False),
        (10, False),
        (11, True),
        (12, False),
        (13, True),
        (14, False),
        (15, False),
        (16, False),
        (17, True),
        (18, False),
        (19, True),
        (20, False),
        (999931, True),
        (512461, False)
    ]
)
def test_eratosthenes_sieve(i, expected):
    actual = primes[i]
    assert actual == expected
