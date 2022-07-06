# Silnie spójne składowe


def DFSscc(G):
    n = len(G)
    v = [-1] * n
    v_d = []

    for i in range(n):
        if v[i] == -1:
            v_d.reverse()
            v_d = DFSVisit_scc(G, i, v, v_d)

    v_d.reverse()

    for i in range(n):
        v[i] = -1
        for j in range(i + 1, n):
            G[i][j], G[j][i] = G[j][i], G[i][j]

    cycles = []
    for i in v_d:
        if v[i] == -1:
            cycles.append(DFSVisit_scc(G, i, v, []))

    print(cycles)


def DFSVisit_scc(G, u, v, v_d):
    n = len(G)
    v[u] = 1

    for i in range(n):
        if v[i] != 1 and G[u][i] == 1:
            DFSVisit_scc(G, i, v, v_d)

    v_d.append(u)

    return v_d


graph = [[0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]]

DFSscc(graph)
