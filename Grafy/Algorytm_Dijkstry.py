from queue import PriorityQueue
from math import inf


def dijkstry(G, s):
    n = len(G)
    Q = PriorityQueue()

    dp = [inf] * n
    p = [-1] * n

    dp[s] = 0
    Q.put((0, s))

    while not Q.empty():
        u = Q.get()

        for i in range(n):
            if dp[i] > dp[u[1]] + G[u[1]][i] and G[u[1]][i] != 0:
                dp[i] = dp[u[1]] + G[u[1]][i]
                Q.put((dp[i], i))
                p[i] = u[1]

    return dp, p


def dijkstra_M(G, s):
    n = len(G)

    dp = [inf] * n
    p = [-1] * n
    visited = [False] * n

    dp[s] = 0

    for i in range(n):

        u = min_distance(dp, visited)
        visited[u] = True

        for j in range(n):
            if dp[j] > dp[u] + G[u][j] and G[u][j] != 0 and visited[j] is False:
                dp[j] = dp[u] + G[u][j]
                p[j] = u

    return dp, p


def min_distance(dp, visited):
    min_w, min_idx, n = inf, 0, len(dp)

    for i in range(n):
        if dp[i] < min_w and visited[i] is False:
            min_w = dp[i]
            min_idx = i

    return min_idx


G = [[0, 1, 5, 0, 0],
     [1, 0, 2, 7, 8],
     [5, 2, 0, 0, 3],
     [0, 7, 0, 0, 1],
     [0, 8, 3, 1, 0]]

G_ns = [[0, 1, 5, 0, 0],
        [1, 0, 2, 7, 8],
        [5, 2, 0, 0, 3],
        [0, 7, 0, 0, 1],
        [0, 8, 3, 1, 0]]

print(dijkstry(G, 0))
print(dijkstra_M(G, 3))
