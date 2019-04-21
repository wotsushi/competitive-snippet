def code(input, _N):
    _A, _B = (
        zip(*(map(int, input().split()) for _ in range(_N))) if _N else
        ((), ())
    )
    return _A, _B
