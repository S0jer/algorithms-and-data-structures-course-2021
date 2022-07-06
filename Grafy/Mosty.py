# Mosty

from math import inf


def DFS_Bridge(G):
    n = len(G)
    v, low, numbers, bridges, v_p = [-1] * n, [inf] * n, [-1] * n, [], [-1] * n
    num = 1

    for i in range(n):
        if v[i] == -1:
            DFSVisit_Bridge(G, i, v, v_p, low, numbers, num, bridges)

    return low, bridges


def DFSVisit_Bridge(G, u, v, v_p, low, numbers, num, bridges):
    v[u], numbers[u], low[u] = 1, num, num
    num += 1

    n = len(G)
    for i in range(n):
        if v[i] != 1 and G[u][i] == 1:
            v_p[i] = u
            DFSVisit_Bridge(G, i, v, v_p, low, numbers, num, bridges)
            low[u] = min(low[u], low[i])
            if low[i] > numbers[u]:
                bridges.append((u, i))

        elif G[u][i] == 1 and i != v_p[u]:
            low[u] = min(low[u], numbers[i])


G = [[0, 1, 1, 0, 0, 0],
     [1, 0, 1, 1, 0, 0],
     [1, 1, 0, 0, 0, 0],
     [0, 1, 0, 0, 1, 1],
     [0, 0, 0, 1, 0, 1],
     [0, 0, 0, 1, 1, 0]]

graph = [[0, 1, 0, 0, 1, 0, 0, 0],
         [1, 0, 1, 0, 0, 0, 0, 0],
         [0, 1, 0, 1, 1, 0, 0, 0],
         [0, 0, 1, 0, 0, 1, 1, 0],
         [1, 0, 1, 0, 0, 0, 0, 1],
         [0, 0, 0, 1, 0, 0, 1, 0],
         [0, 0, 0, 1, 0, 1, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0]]
# ([1, 1, 1, 4, 1, 4, 4, 8], [(2, 3), (4, 7)])
print(DFS_Bridge(graph))
