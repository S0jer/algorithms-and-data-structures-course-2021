# Zadanie 3. (najkrósze ścieżki w DAGu) Jak znaleźć najkrótsze ścieżki z wierzchołka s do wszystkich
# innych w acyklicznym grafie skierowanym?

from queue import PriorityQueue
from math import inf


def shortest_path(G):
    dp = DFS_TpK(G)
    s = dp[0]

    dp, p = dijkstry(G, s)

    return s, dp


def dijkstry(G, s):
    Q = PriorityQueue()

    n = len(G)
    dp = [inf] * n
    p = [-1] * n

    dp[s] = 0
    Q.put((0, s))

    while not Q.empty():
        u = Q.get()

        for i in G[u[1]]:
            if dp[i[0]] > dp[u[1]] + i[1]:
                dp[i[0]] = dp[u[1]] + i[1]
                Q.put((dp[i[0]], i[0]))
                p[i[0]] = u[1]

    return dp, p


def DFS_TpK(G):
    n = len(G)
    v = [-1] * n
    delete = []

    i = 0
    while i != n:
        delete, v = DFSVisit_TpK(G, i, v, delete)
        while i != n and v[i] != -1:
            i += 1

    return delete[::-1]


def DFSVisit_TpK(G, u, v, delete):
    v[u] = 1

    for i in G[u]:
        if v[i[0]] != 1:
            DFSVisit_TpK(G, i[0], v, delete)

    delete.append(u)

    return delete, v


graph = [
    [(6, 4)],
    [(3, 5)],
    [(0, 2), (1, 7)],
    [(0, 4), (5, 2)],
    [(2, 1)],
    [],
    [(5, 0)]]

print(shortest_path(graph))
