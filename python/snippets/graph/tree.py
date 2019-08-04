def code():
    def tree(G, r):
        p = [i for i in range(len(G))]
        c = [set() for _ in range(len(G))]
        q = []
        c[r] = G[r]
        q.append(r)
        while q:
            i = q.pop()
            for j in G[i]:
                if j != p[i]:
                    p[j] = i
                    c[j] = G[j] - {i}
                    q.append(j)
        return p, c
    return tree
