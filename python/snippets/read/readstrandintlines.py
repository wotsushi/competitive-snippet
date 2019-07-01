def code(input, _N):
    _S, _A = (
        zip(*(
            (s, int(n))
            for s, n in (input().split() for _ in range(_N))
        )) if _N else
        ((), ())
    )
    return _S, _A
