def code(input, _N):
    _S, _T = (
        zip(*(input().split() for _ in range(_N))) if _N
        else ((), ())
    )
    return _S, _T
