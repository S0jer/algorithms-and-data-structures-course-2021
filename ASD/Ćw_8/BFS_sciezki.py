import queue


def BFS(G, s):
    n = len(G)
    Q = queue.Queue()

    list = []

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

    return v, v_d, list


G = [[0, 1, 1, 0, 0, 0],
     [1, 0, 1, 1, 0, 1],
     [1, 1, 0, 0, 1, 1],
     [0, 1, 0, 0, 0, 1],
     [0, 0, 1, 0, 0, 1],
     [0, 1, 1, 1, 1, 0]]


v, v_d, list = BFS(G, 2)

print(v)
print(v_d)
print(list)
