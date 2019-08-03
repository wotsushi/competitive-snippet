def code():
    def tree(G, r):
        res = [None for _ in range(len(G))]
        q = []
        res[r] = (r, G[r])
        q.append(r)
        while q:
            i = q.pop()
            for j in G[i]:
                if res[j] is None:
                    res[j] = (i, G[j] - {i})
                    q.append(j)
        return res
    return tree
