def code():
    def topological_sort(G):
        n = len(G) - 1
        d = [0 for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in G[i]:
                d[j] += 1
        res = [i for i in range(1, n + 1) if d[i] == 0]
        for i in range(n):
            for j in G[res[i]]:
                d[j] -= 1
                if d[j] == 0:
                    res.append(j)
        return res
    return topological_sort
