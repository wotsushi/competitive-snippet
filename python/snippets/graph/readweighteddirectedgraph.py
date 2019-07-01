def code(_N, _a, _b, _c):
    _G = [{} for _ in range(_N + 1)]
    for x, y, w in zip(_a, _b, _c):
        _G[x][y] = w
    return _G
