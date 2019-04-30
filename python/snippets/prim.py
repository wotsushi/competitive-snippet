from heapq import heappush, heappop


def code():
    def prim(G):
        used = [False for _ in range(len(G))]
        res = 0
        q = []
        used[1] = True
        for j, w in G[1].items():
            heappush(q, (w, j))
        while q:
            w, j = heappop(q)
            if not used[j]:
                used[j] = True
                res += w
                for j2, w2 in G[j].items():
                    heappush(q, (w2, j2))
        return res
    return prim
