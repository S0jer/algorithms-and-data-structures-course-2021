# Paweł Jaśkowiec, 406165

# Pomysł polega na wyznaczeniu odleglości miedzy wierzchołkami za pomocą algorytmu Floyd'a - Warshall'a
# a następnie wyznaczenie trasy za pomocą algorytmu podobnego do dijkstry z tą modyfikacją że w kolejce sortuje
# po odległości od celu dla x, przy czym gdy tylko to mozliwe przesuwam y w kierunku konca


from zad1testy import runtests

from collections import deque
from math import inf
from copy import deepcopy

from math import inf
from collections import deque


def keep_distance(tab, x, y, d):
    def floyd_warshall_algorithm(tab):
        n = len(tab)
        for x in range(n):
            distance[x][x] = 0
        for x in range(n):
            for y in range(n):
                if tab[x][y] != 0:
                    distance[x][y] = tab[x][y]

        for k in range(n):
            for u in range(n):
                for v in range(n):
                    if distance[u][v] > distance[u][k] + distance[k][v]:
                        distance[u][v] = distance[u][k] + distance[k][v]
        return distance

    def print_solution(parent, x, y, a, b):
        nonlocal set1
        while (x, y) != (a, b):
            set1.append((x, y))
            (x, y) = parent[x][y]
        set1.append((a, b))
        return set1[::-1]

    n = len(tab)
    Q = deque()
    set1 = []
    distance = [[inf for _ in range(n)] for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]
    parent = [[(-1, -1) for _ in range(n)] for _ in range(n)]
    visited[x][y] = True
    distance = floyd_warshall_algorithm(tab)
    Q.append((x, y))
    (a, b) = (x, y)

    while True:
        u, v = Q.popleft()
        for x in range(n):
            if tab[u][x] != 0:
                for y in range(n):
                    if tab[v][y] != 0:
                        if (u, v) != (y, x) and distance[x][y] >= d and visited[x][y] is False:
                            Q.append((x, y))
                            parent[x][y] = (u, v)
                            visited[x][y] = True
                            if (y, x) == (a, b):
                                return print_solution(parent, x, y, a, b)

        for y in range(n):
            if tab[v][y] != 0:
                if y != u and distance[u][y] >= d and visited[u][y] is False:
                    Q.append((u, y))
                    parent[u][y] = (u, v)
                    visited[u][y] = True
                    if (y, u) == (a, b):
                        return print_solution(parent, u, y, a, b)

        for x in range(n):
            if tab[u][x] != 0:
                if x != v and distance[x][v] >= d and visited[x][v] is False:
                    Q.append((x, v))
                    parent[x][v] = (u, v)
                    visited[x][v] = True
                    if (v, x) == (a, b):
                        return print_solution(parent, x, v, a, b)


def floyd_warshall(G):
    n = len(G)

    dp = [[inf] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if G[i][j] != 0:
                dp[i][j] = G[i][j]
            else:
                dp[i][j] = inf

    for t in range(n):
        for u in range(n):
            for w in range(n):
                if u != w:
                    dp[u][w] = min(dp[u][w], dp[u][t] + dp[t][w])

    return dp


M2 = [[0, 5, 1, 0, 0, 0],
      [5, 0, 0, 5, 0, 0],
      [1, 0, 0, 1, 0, 0],
      [0, 5, 1, 0, 1, 0],
      [0, 0, 0, 1, 0, 1],
      [0, 0, 0, 0, 1, 0]]
x2 = 0
y2 = 5
d2 = 4
z2 = [0, 5, 0, 1, 6, 0, 2, 5, 1, 0, 3, 6, 2, 1, 0, 4, 7, 3, 2, 1, 0]

# print(keep_distance(M2, x2, y2, d2))

runtests(keep_distance)
