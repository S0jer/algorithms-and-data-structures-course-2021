# Topologiczne sortowanie na listach


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


graph = [[1, 2], [2, 3], [], [4, 5, 6], [], [], [], [3], [7]]

print(DFS_TpK(graph))
