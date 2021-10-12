import queue


def BFS_K(G, s):
    n = len(G)
    Q = queue.Queue()

    v = [-1] * n
    v_parent = [-1] * n
    v_d = [-1] * n

    v_d[s] = 0
    v[s] = 1
    Q.put(s)

    while not Q.empty():
        u = Q.get()
        for i in G[u]:
            if v[i] != 1:
                v[i] = 1
                v_d[i] = v_d[u] + 1
                v_parent[i] = u
                Q.put(i)

    return v, v_d

graph = [[1, 2], [2, 3], [], [4, 5, 6], [], [], [], [3], [7]]
BFS_K(graph, 0)


