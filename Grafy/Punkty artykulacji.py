# Punkty artykulacji

from math import inf


def DFS_Arcticulation(G):
    n = len(G)
    v, low, numbers, arct, v_p = [-1] * n, [inf] * n, [inf] * n, [False] * n, [-1] * n
    num = 0

    for i in range(n):
        if v[i] == -1:
            low, numbers, v_p, v, num, arct = DFSV_Arct(G, i, v, v_p, low, numbers, num, arct)

    print(arct)
    return low, arct


def DFSV_Arct(G, u, v, v_p, low, numbers, num, arct):
    n = len(G)
    v[u], numbers[u], low[u] = 1, num, num
    num += 1
    children = 0

    for i in range(n):
        if v[i] != 1 and G[u][i] == 1:
            children += 1

            v_p[i] = u
            low, numbers, v_p, v, num, arct = DFSV_Arct(G, i, v, v_p, low, numbers, num, arct)

            low[u] = min(low[u], low[i])

            if v_p[u] == -1 and children > 1:
                arct[u] = True

            if v_p[u] != -1 and low[i] >= numbers[u]:
                arct[u] = True

        elif i != v_p[u] and G[u][i] == 1:
            low[u] = min(low[u], numbers[i])

    return low, numbers, v_p, v, num, arct



graph = [[0, 1, 1, 1, 0, 0],
         [1, 0, 1, 0, 0, 0],
         [1, 1, 0, 0, 0, 0],
         [1, 0, 0, 0, 1, 1],
         [0, 0, 0, 1, 0, 1],
         [0, 0, 0, 1, 1, 0]]



DFS_Arcticulation(graph)
