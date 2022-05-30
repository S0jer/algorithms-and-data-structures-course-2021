# Zad. 1. Dany jest spójny graf nieskierowany G = (V,E). Proszę
# zaproponować algorytm, który znajdzie taką kolejność usuwania
# wierzchołków, która powoduje że w trakcie usuwania graf nigdy nie
# przestaje być spójny (usunięcie wierzchołka usuwa, oczywiście, wszystkie
# dotykające go krawędzie).


def DFS(G):
    n = len(G)
    v = [-1] * n
    delete = []

    delete = DFSVisit(G, 0, v, delete)

    return delete


def DFSVisit(G, u, v, delete):
    v[u] = 1
    n = len(G)
    for i in range(n):
        if v[i] != 1 and G[u][i] == 1:
            DFSVisit(G, i, v, delete)

    delete.append(u)

    return delete


G = [[0, 1, 1, 0, 0, 0],
     [1, 0, 1, 1, 0, 1],
     [1, 1, 0, 0, 1, 1],
     [0, 1, 0, 0, 0, 1],
     [0, 0, 1, 0, 0, 1],
     [0, 1, 1, 1, 1, 0]]

G_1 = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
       [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
       [1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 0, 1, 1, 1, 1, 0, 1],
       [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
       [0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
       [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
       [0, 0, 0, 1, 0, 0, 0, 0, 1, 0]]

G_2 = [[0, 1, 1, 0, 0, 0, 0, 0],
       [1, 0, 0, 1, 0, 0, 0, 0],
       [1, 0, 0, 0, 1, 0, 0, 0],
       [0, 1, 0, 0, 1, 0, 0, 0],
       [0, 0, 1, 1, 0, 1, 0, 0],
       [0, 0, 0, 0, 1, 0, 1, 0],
       [0, 0, 0, 0, 0, 1, 0, 1],
       [0, 0, 0, 0, 0, 0, 1, 0]]

d = DFS(G)
print(d)
d = DFS(G_1)
print(d)
d = DFS(G_2)
print(d)
