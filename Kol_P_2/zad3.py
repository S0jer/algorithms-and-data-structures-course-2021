from zad3testy import runtests
from queue import PriorityQueue
from math import inf

global e


def paths(G, s, t):
    return dijkstry(G, s, t)


def dijkstry(G, s, t):
    global e
    e = 0
    n = len(G)
    Q = PriorityQueue()

    dp = [inf for _ in range(n)]
    p = [[] for _ in range(n)]

    dp[s] = 0
    Q.put((0, s))

    while not Q.empty():
        u = Q.get()

        for i in range(len(G[u[1]])):
            if dp[G[u[1]][i][0]] > dp[u[1]] + G[u[1]][i][1]:
                dp[G[u[1]][i][0]] = dp[u[1]] + G[u[1]][i][1]
                Q.put((dp[G[u[1]][i][0]], G[u[1]][i][0]))
                p[G[u[1]][i][0]] = [u[1]]

            elif dp[G[u[1]][i][0]] == dp[u[1]] + G[u[1]][i][1]:
                # Q.put((dp[G[u[1]][i][0]], G[u[1]][i][0]))
                p[G[u[1]][i][0]].append(u[1])

    v = [[-1 for _ in range(n)] for _ in range(n)]
    res(p, v, t, s)

    return e


def res(p, v, t, s):
    global e
    if t == s:
        return

    for i in p[t]:
        if v[i][t] == -1 and v[t][i] == -1:
            e += 1
            v[i][t] = 1
            v[t][i] = 1
            res(p, v, i, s)


runtests(paths)
