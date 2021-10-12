# Algorytm Kruskala

def kruskal(G):
    n = len(G)
    E = []
    A = []

    for i in range(n):
        for j in range(n):
            if G[i][j] != 0:
                E.append(((i, j), G[i][j]))
                G[i][j] = 0
                G[j][i] = 0

    E.sort(key=lambda E: E[1])

    m = len(E)
    v_p = [i for i in range(m)]
    rank = [0] * m

    for i in range(m):
        if find(E[i][0][0], v_p) != find(E[i][0][1], v_p):
            union(E[i][0][0], E[i][0][1], v_p, rank)
            A.append(E[i][0])

    print(A)
    return A


def union(x, y, v_p, rank):
    x = find(x, v_p)
    y = find(y, v_p)

    if x == y: return 1
    if rank[x] > rank[y]:
        v_p[y] = x
    else:
        v_p[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1


def find(x, v_p):
    if x != v_p[x]:
        v_p[x] = find(v_p[x], v_p)
    return v_p[x]


G = [[0, 1, 5, 0, 0],
     [1, 0, 2, 7, 8],
     [5, 2, 0, 0, 3],
     [0, 7, 0, 0, 1],
     [0, 8, 3, 1, 0]]

kruskal(G)
