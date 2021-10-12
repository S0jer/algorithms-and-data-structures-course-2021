from queue import PriorityQueue
from math import inf

def dijkstry(G, s):
    n = len(G)
    Q = PriorityQueue()

    v = [-1] * n
    d = [inf] * n
    p = [-1] * n

    d[s] = 0
    v[s] = 1
    Q.put((0, s))

    while not Q.empty():
        u = Q.get()
        v[u[1]] = 1
        for i in range(n):
            if G[u[1]][i] != 0:
                v[i] = 1
            if G[u[1]][i] != 0 and v[i] == -1:
                d[i] = min(d[u[1]], G[u[1]][i], d[i])
                p[i] = u[1]
                Q.put((G[u[1]][i], i))

    print(d)
    print(p)
    return d, p


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


dijkstry(G, 0)
