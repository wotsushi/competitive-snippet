from heapq import heappush, heappop


def code(_INF):
    def dijkstra(G, s):
        dp = [_INF for _ in range(len(G))]
        q = []
        heappush(q, (0, s))
        while q:
            c, i = heappop(q)
            if dp[i] == _INF:
                dp[i] = c
                for j, w in G[i].items():
                    heappush(q, (c + w, j))
        return dp
    return dijkstra
