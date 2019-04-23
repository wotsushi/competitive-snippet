import unittest
from snippets import eratosthenes_sieve


class TestReadInt(unittest.TestCase):
    def test_prime_numbers_leq_20(self):
        primes = eratosthenes_sieve.code(20)
        self.assertEqual(
            primes,
            [
                False,
                False,
                True,
                True,
                False,
                True,
                False,
                True,
                False,
                False,
                False,
                True,
                False,
                True,
                False,
                False,
                False,
                True,
                False,
                True,
                False
            ]
        )

    def test_large_prime_number(self):
        primes = eratosthenes_sieve.code(10**6)
        self.assertTrue(
            primes[999931],
        )

    def test_carmichael_number(self):
        primes = eratosthenes_sieve.code(10**6)
        self.assertFalse(
            primes[512461],
        )
