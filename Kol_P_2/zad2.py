from zad2testy import runtests


def order(L, K):
    result = DFS_Tp(L, K)

    return result


def DFS_Tp(G, K):
    n = len(G)
    v = [-1] * n
    delete = []

    i = 0
    X = 10 ** K
    while i != n - 1:
        delete, v = DFSVisit_Tp(G, i, v, delete, X)
        while i != n - 1 and v[i] != -1:
            i += 1

    return delete[::-1]


def DFSVisit_Tp(G, u, v, delete, X):
    v[u] = 1
    n = len(G)

    for i in range(n):
        if v[i] != 1 and G[u] % X == G[i] // X:
            DFSVisit_Tp(G, i, v, delete, X)

    delete.append(G[u])

    return delete, v


runtests(order)
