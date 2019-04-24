def code(_N, _a, _b):
    _G = [set() for _ in range(_N + 1)]
    for x, y in zip(_a, _b):
        _G[x].add(y)
    return _G
