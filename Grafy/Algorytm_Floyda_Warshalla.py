# Algorytm Floyda-Warshalla
from math import inf


def floyd_warshall(G, W):
    n = len(G)

    d = [[inf] * n for _ in range(n)]
    p = [[-1] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if W[i][j] != 0:
                d[i][j] = W[i][j]
            else:
                d[i][j] = inf

    for t in range(n):
        for u in range(n):
            for w in range(n):
                if u != w:
                    d[u][w] = min(d[u][w], d[u][t] + d[t][w])

    return d


def floyd_warshall_P(G, W):
    n = len(G)

    d = [[inf] * n for _ in range(n)]
    p = [[-1] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if W[i][j] != 0:
                d[i][j] = W[i][j]
                p[i][j] = i

    for t in range(n):
        for u in range(n):
            for w in range(n):
                if u != w and d[u][w] > d[u][t] + d[t][w]:
                    d[u][w] = d[u][t] + d[t][w]
                    p[u][w] = p[t][w]

    for a in p:
        print(a)

    return d


G = [[0, 1, 0, 0, 0, 1],
     [1, 0, 1, 0, 0, 1],
     [0, 1, 0, 1, 0, 1],
     [0, 0, 1, 0, 1, 0],
     [0, 0, 0, 1, 0, 1],
     [1, 1, 1, 0, 1, 0]]

W = [[0, 4, 0, 0, 0, 3],
     [4, 0, 2, 0, 0, 4],
     [0, 2, 0, 4, 0, 2],
     [0, 0, 4, 0, 5, 0],
     [0, 0, 0, 5, 0, 7],
     [3, 4, 2, 0, 7, 0]]

print(floyd_warshall_P(G, W))
