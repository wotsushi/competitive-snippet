def code():
    class SegmentTree:
        def __init__(self, n, f, e):
            self.n = 2**((n - 1).bit_length())
            self.f = f
            self.e = e
            self.d = [e for _ in range(2 * self.n)]

        def __setitem__(self, key, value):
            key += self.n - 1
            self.d[key] = value
            while key > 1:
                key //= 2
                self.d[key] = self.f(self.d[2 * key], self.d[2 * key + 1])

        def __getitem__(self, key):
            return self.q(key, 1, 1, self.n + 1)

        def q(self, key, i, left, right):
            return (
                self.e if left >= key.stop or right <= key.start else
                self.d[i] if key.start <= left <= right <= key.stop else
                self.f(
                    self.q(key, 2 * i, left, (left + right) // 2),
                    self.q(key, 2 * i + 1, (left + right) // 2, right)
                )
            )

    return SegmentTree
