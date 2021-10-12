from queue import Queue



def tasks(T):
    n = len(T)
    G = T_to_G(T)

    for i in range(n):
        road = BFS(G, i)



def BFS(G, s):
    n = len(G)
    Q = Queue()


    v = [-1] * n
    v_parent = [-1] * n
    v_d = [-1] * n

    v_d[s] = 0
    v[s] = 1
    Q.put(s)

    while not Q.empty():
        u = Q.get()
        for i in range(n):
            if v[i] != 1 and G[u][i] == 1:
                v[i] = 1
                v_d[i] = v_d[u] + 1
                v_parent[i] = u
                Q.put(i)

    return v_parent


def T_to_G(T):
    n = len(T)
    G = [[-1] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i != j and T[i][j] == 1 and T[j][i] != 1:
                G[i][j] = 1
            elif i != j and T[i][j] == 2 and T[j][i] != 2:
                G[j][i] = 1
            elif i != j and T[i][j] == 0:
                G[i][j] = 1

    return G


T = [[0, 2, 1, 1], [1, 0, 1, 1], [2, 2, 0, 1], [2, 2, 2, 0]]

print(tasks(T))
