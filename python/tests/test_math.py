from snippets.math import eratosthenes_sieve
from parameterized import parameterized

primes = eratosthenes_sieve.code(10**6)


@parameterized.expand(
    [
        (
            0,
            False
        ),
        (
            1,
            False
        ),
        (
            2,
            True
        ),
        (
            3,
            True
        ),
        (
            4,
            False
        ),
        (
            5,
            True
        ),
        (
            6,
            False
        ),
        (
            7,
            True
        ),
        (
            8,
            False
        ),
        (
            9,
            False
        ),
        (
            10,
            False
        ),
        (
            11,
            True
        ),
        (
            12,
            False
        ),
        (
            13,
            True
        ),
        (
            14,
            False
        ),
        (
            15,
            False
        ),
        (
            16,
            False
        ),
        (
            17,
            True
        ),
        (
            18,
            False
        ),
        (
            19,
            True
        ),
        (
            20,
            False
        ),
        (
            999931,
            True
        ),
        (
            512461,
            False
        )
    ]
)
def test_eratosthenes_sieve(i, expected):
    actual = primes[i]
    assert actual == expected
