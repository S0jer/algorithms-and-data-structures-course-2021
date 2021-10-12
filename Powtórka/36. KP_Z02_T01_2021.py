from zad2testy import runtests
from math import inf


def breaking(G):
    n = len(G)
    b_count = [0] * n
    arct, bridges = DFS_Arcticulation(G)

    for i in range(len(bridges)):
        b_count[bridges[i][0]] += 1
        b_count[bridges[i][1]] += 1

    cnt, result = -1, -1
    for j in range(n):
        if arct[j] is True and b_count[j] > cnt:
            cnt = b_count[j]
            result = j

    if result != -1:
        return result

    return None


def DFS_Arcticulation(G):
    n = len(G)
    v, low, numbers, arct, v_p, bridges = [-1] * n, [inf] * n, [inf] * n, [False] * n, [-1] * n, []
    num = 0

    for i in range(n):
        if v[i] == -1:
            low, numbers, v_p, v, num, arct = DFSV_Arct(G, i, v, v_p, low, numbers, num, arct)

    for i in range(n):
        if low[i] == numbers[i] and v_p[i] != -1:
            bridges.append((v_p[i], i))

    return arct, bridges


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


runtests(breaking)


