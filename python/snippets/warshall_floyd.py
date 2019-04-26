def code(_INF):
    def warshall_floyd(G):
        dp = [
            [
                0 if i == j else
                G[i][j] if j in G[i] else
                _INF
                for j in range(len(G))
            ]
            for i in range(len(G))
        ]
        for k in range(len(G)):
            for i in range(len(G)):
                for j in range(len(G)):
                    dp[i][j] = (
                        dp[i][j] if dp[i][k] == _INF or dp[k][j] == _INF else
                        min(dp[i][j], dp[i][k] + dp[k][j])
                    )
        return dp
    return warshall_floyd
