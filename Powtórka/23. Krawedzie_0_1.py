# Zadanie 5. (krawędzie 0/1) Dana jest mapa kraju w postaci grafu G = (V, E). Kierowca chce przejechać
# z miasta (wierzchołka) s to miasta t. Niestety niektóre drogi (krawędzie) są płatne. Każda droga ma taką 1
# samą jednostkową opłatę. Proszę podać algorytm, który znajduje trasę wymagającą jak najmniejszej liczby
# opłat. W ogólności graf G jest skierowany, ale można najpierw wskazać algorytm dla grafu nieskierowanego.


from math import inf
import queue


def road(M, s, t):
    result, v_parents = BFS(M, s, t)

    path = get_road(v_parents, s, t)

    return result, path


def BFS(G, s, t):
    n = len(G)
    Q = queue.Queue()

    v = [-1] * n
    costs = [inf] * n
    v_parent = [-1] * n

    costs[s] = 0
    v[s] = 1
    Q.put(s)

    while not Q.empty():
        u = Q.get()
        for i in range(n):
            if v[i] != 1 and G[u][i] != -1:
                v[i] = 1
                Q.put(i)
            if G[u][i] != -1 and costs[u] + G[u][i] < costs[i]:
                costs[i] = costs[u] + G[u][i]
                v_parent[i] = u

    return costs[t], v_parent


def get_road(v_parents, s, t):
    road = [t]
    curr = t
    while curr != s:
        curr = v_parents[curr]
        road.append(curr)

    return road[::-1]


G = [[-1, 1, 1, -1, -1],
     [1, -1, 1, -1, -1],
     [-1, 1, -1, 0, -1],
     [-1, -1, 0, -1, 1],
     [-1, -1, -1, 1, -1]]

result, path = road(G, 0, 4)

print(result)
print(path)
