def bellman_ford(G, s):
    n = len(G)
    dp = [100000] * n
    p = [-1] * n

    dp[s] = 0

    for k in range(n - 1):
        for i in range(n):
            for j in range(n):
                if G[i][j] != 0:
                    relax(G, p, dp, i, j)

    for i in range(n):
        for j in range(n):
            if dp[i] > dp[j] + G[i][j] and G[i][j] != 0:
                return None

    return dp


def relax(G, p, dp, u, v):
    if dp[v] > dp[u] + G[u][v]:
        dp[v] = dp[u] + G[u][v]
        p[v] = u


G = [[0, 1, 5, 0, 0],
     [1, 0, 2, 7, 8],
     [5, 2, 0, 0, 3],
     [0, 7, 0, 0, 1],
     [0, 8, 3, 1, 0]]

G2 = [[0, 1, 2, 3, 0],
      [0, 0, 0, 2, 4],
      [0, 0, 0, 0, 3],
      [0, 0, 1, 0, 1],
      [0, 0, 0, 0, 0]]

G3 = [[0, -1, 0],
      [0, 0, -1],
      [-1, 0, 0]]

print(bellman_ford(G, 0))
print(bellman_ford(G2, 0))
print(bellman_ford(G3, 0))
