# Proszę zaimplementować algorytm sprawdzający czy graf jest dwudzielny.

import queue


def BFS(G, s):
    n = len(G)
    Q = queue.Queue()

    v = [-1] * n
    col = [0] * n

    v[s] = 1
    col[s] = 1
    Q.put(s)

    while not Q.empty():
        u = Q.get()
        for i in range(n):
            if v[i] != 1 and G[u][i] == 1:
                v[i] = 1
                Q.put(i)
            if col[u] == 1 and G[u][i] == 1:
                if col[i] == 1:
                    return False
                col[i] = -1
            elif col[u] == -1 and G[u][i] == 1:
                if col[i] == -1:
                    return False
                col[i] = 1

    return True


G = [[0, 1, 1, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 1, 0, 0, 0],
     [1, 0, 0, 1, 0, 1, 0, 0],
     [0, 0, 1, 0, 1, 0, 0, 0],
     [0, 1, 0, 1, 0, 1, 0, 0],
     [0, 0, 1, 0, 1, 0, 1, 0],
     [0, 0, 0, 0, 0, 1, 0, 1],
     [0, 0, 0, 0, 0, 0, 1, 0]]

graph = [[0, 1, 0, 0],
         [1, 0, 1, 0],
         [0, 0, 0, 1],
         [0, 0, 1, 0]]

print(BFS(graph, 0))
print(BFS(G, 0))
