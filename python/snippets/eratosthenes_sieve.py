def code(_N):
    primes = [True for _ in range(_N + 1)]
    primes[0] = primes[1] = False
    for i in range(2, _N + 1):
        if primes[i]:
            for j in range(2 * i, _N + 1, i):
                primes[j] = False
    return primes
