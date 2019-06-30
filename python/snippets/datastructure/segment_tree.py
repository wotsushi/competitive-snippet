def code():
    class SegmentTree:
        def __init__(self, n, f, e):
            def v(i, j):
                return (
                    [i, j, e] if j == i + 1 else
                    [
                        i,
                        j,
                        v(i, (i + j) // 2),
                        v((i + j) // 2, j),
                        e
                    ]
                )
            self.n = 2**((n - 1).bit_length())
            self.r = v(1, self.n + 1)
            self.f = f
            self.e = e

        def __setitem__(self, key, value):
            def u(v):
                if v[1] == v[0] + 1:
                    v[-1] = value
                else:
                    u(
                        v[2] if key < (v[0] + v[1]) // 2 else
                        v[3]
                    )
                    v[-1] = self.f(v[2][-1], v[3][-1])
            u(self.r)

        def __getitem__(self, key):
            def q(v):
                return (
                    self.e if v[0] >= key.stop or v[1] <= key.start else
                    v[-1] if key.start <= v[0] <= v[1] <= key.stop else
                    self.f(q(v[2]), q(v[3]))
                )
            return q(self.r)

    return SegmentTree
