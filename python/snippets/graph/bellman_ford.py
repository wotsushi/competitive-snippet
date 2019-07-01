def code(_INF):
    def bellman_ford(G, s):
        dp = [_INF for _ in range(len(G))]
        dp[s] = 0
        for _ in range(len(G)):
            for i in range(len(G)):
                for j, w in G[i].items():
                    dp[j] = min(dp[j], dp[i] + w)
        return dp
    return bellman_ford
