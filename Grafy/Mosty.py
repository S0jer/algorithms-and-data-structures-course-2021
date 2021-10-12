# Mosty

from math import inf


def DFS_Bridge(G):
    n = len(G)
    v, low, numbers, bridges, v_p = [-1] * n, [inf] * n, [-1] * n, [], [-1] * n
    num = 1

    for i in range(n):
        if v[i] == -1:
            low, numbers, v_p, num = DFSVisit_Bridge(G, i, v, v_p, low, numbers, num)

    for i in range(n):
        if low[i] == numbers[i] and v_p[i] != -1:
            bridges.append((v_p[i], i))

    return low, bridges


def DFSVisit_Bridge(G, u, v, v_p, low, numbers, num):
    v[u], numbers[u], low[u] = 1, num, num

    n = len(G)
    for i in range(n):

        if v[i] == 1 and G[u][i] == 1 and i != v_p[u]:
            low[u] = min(numbers[u], numbers[i])

        if v[i] != 1 and G[u][i] == 1:
            num += 1
            v_p[i] = u
            low, numbers, v_p, num = DFSVisit_Bridge(G, i, v, v_p, low, numbers, num)

    for i in range(n):
        if v[i] == 1 and G[u][i] == 1 and i != v_p[u]:
            low[u] = min(low[u], low[i])

    return low, numbers, v_p, num


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

print(DFS_Bridge(graph))
