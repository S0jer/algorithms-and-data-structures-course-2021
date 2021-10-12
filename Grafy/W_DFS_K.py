


def DFS_K(G):
    n = len(G)
    v = [-1] * n
    v_p = [-1] * n

    for i in range(n):
        if v[i] == -1:
            DFSVisit_K(G, i, v, v_p)


def DFSVisit_K(G, u, v, v_p):
    v[u] = 1

    for i in G[u]:
        if v[i] != 1:
            v_p[i] = u
            DFSVisit_K(G, i, v, v_p)


graph = [[1, 2], [2, 3], [], [4, 6], [], [], [], [3], [7]]

print(DFS_K(graph))
