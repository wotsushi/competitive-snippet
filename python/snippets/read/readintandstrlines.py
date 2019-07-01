def code(input, _N):
    _A, _S = (
        zip(*(
            (int(n), s)
            for n, s in (input().split() for _ in range(_N))
        )) if _N else
        ((), ())
    )
    return _A, _S
