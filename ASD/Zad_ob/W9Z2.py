# Zad. 2. Proszę podać jak najszybszy algorytm, który znajduje w grafie
# cykl długości dokładnie 4 (trywialny algorytm ma złożoność O(n^4), gdzie
# n to liczba wierzchołków---chodzi o rozwiązanie szybsze).

import queue


def find_cycle(G, k):
    n = len(G)
    suma = 0

    for i in G:
        suma += sum(i)

    if suma == n ** 2:
        return [1, 2, 3, 4]

    cycle = []
    i = 0

    while len(cycle) != k + 1 and i < n:
        cycle = BFS(G, i, k)
        i += 1

    if len(cycle) < k:
        return None
    return cycle


def BFS(G, s, k):
    n = len(G)
    Q = queue.Queue()

    v = [-1] * n
    v_parent = [-1] * n
    v_d = [0] * n

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
            elif v[i] == 1 and G[u][i] == 1 and v_d[i] == k - 1 and v_d[u] == k - 2:
                return [s, v_parent[u], u, i, s]

    return []


G = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
     [1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 1, 1, 1, 1, 0, 1],
     [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
     [0, 0, 0, 1, 0, 0, 0, 0, 1, 0]]

G3 = [[0, 1, 1, 1, 1],
      [1, 0, 1, 1, 1],
      [1, 1, 0, 0, 1],
      [1, 1, 0, 0, 1],
      [1, 1, 1, 1, 0]]

print(find_cycle(G, 4))
print()
print(find_cycle(G3, 4))
