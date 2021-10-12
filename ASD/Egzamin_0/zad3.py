from zad3testy import runtests
from math import inf


def jumper(G, s, w):
    result = dijkstra_M(G, s, w)
    return result


def dijkstra_M(G, s, w):
    n = len(G)

    dp = [[inf, inf] for _ in range(n)]
    visited = [False] * n

    dp[s][0], dp[s][1] = 0, 0

    for i in range(n):

        u = min_distance(dp, visited)
        visited[u] = True

        for j in range(n):
            if dp[j][0] > dp[u][0] + G[u][j] and G[u][j] != 0 and visited[j] is False:
                dp[j][0] = dp[u][0] + G[u][j]
                for z in range(n):

                    if dp[z][1] > dp[u][0] + max(G[j][z], G[u][j]) and G[j][z] != 0 and visited[z] is False:
                        dp[z][1] = dp[u][0] + max(G[j][z], G[u][j])

            if dp[j][0] > dp[u][1] + G[u][j] and G[u][j] != 0 and visited[j] is False:
                dp[j][0] = dp[u][1] + G[u][j]

    return min(dp[w][0], dp[w][1])


def min_distance(dp, visited):
    min_w, min_idx, n = inf, 0, len(dp)

    for i in range(n):
        if dp[i][0] < min_w and visited[i] is False:
            min_w = dp[i][0]
            min_idx = i
        if dp[i][1] < min_w and visited[i] is False:
            min_w = dp[i][1]
            min_idx = i

    return min_idx


runtests(jumper)
