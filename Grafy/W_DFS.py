


def DFS(G):
    n = len(G)
    v = [-1] * n
    v_p = [-1] * n

    for i in range(n):
        if v[i] == -1:
            DFSVisit(G, i, v, v_p)


def DFSVisit(G, u, v, v_p):
    v[u] = 1
    n = len(G)
    for i in range(n):
        if v[i] != 1 and G[u][i] == 1:
            v_p[i] = u
            DFSVisit(G, i, v, v_p)
