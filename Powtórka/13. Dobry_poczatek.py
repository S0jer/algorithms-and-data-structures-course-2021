# Zadanie 2. (dobry początek) Wierzchołek v w grafie skierowanym nazywamy dobrym początkiem jeśli
# każdy inny wierzchołek można osiągnąć scieżką skierowaną wychodzącą z v. Proszę podać algorytm, który
# stwierdza czy dany graf zawiera dobry początek


def the_good_start(G):
    dp = DFS_TpK(G)

    s = dp[0]

    v = DFS_K(G, s)

    for i in v:
        if i == -1:
            return False

    return True


def DFS_K(G, s):
    n = len(G)
    v = [-1] * n
    v_p = [-1] * n

    DFSVisit_K(G, s, v, v_p)

    return v


def DFSVisit_K(G, u, v, v_p):
    v[u] = 1

    for i in G[u]:
        if v[i] != 1:
            v_p[i] = u
            DFSVisit_K(G, i, v, v_p)


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
        if v[i] != 1:
            DFSVisit_TpK(G, i, v, delete)

    delete.append(u)

    return delete, v


graph = [
    [6],
    [3],
    [0, 1],
    [0, 5],
    [2],
    [],
    [5], ]

print(the_good_start(graph))
