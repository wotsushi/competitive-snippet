def code():
    class UnionFindTree:
        def __init__(self, n):
            self.p = [i for i in range(n + 1)]
            self.r = [1 for _ in range(n + 1)]

        def find(self, x):
            if self.p[x] != x:
                self.p[x] = self.find(self.p[x])
            return self.p[x]

        def union(self, x, y):
            px = self.find(x)
            py = self.find(y)
            if self.r[px] < self.r[py]:
                self.r[py] += self.r[px]
                self.p[px] = py
            else:
                self.r[px] += self.r[py]
                self.p[py] = px

        def same(self, x, y):
            return self.find(x) == self.find(y)

        def size(self, x):
            return self.r[self.find(x)]

    return UnionFindTree
