# Dany jest zbiór N zadań, gdzie niektóre zadania muszą być wykonane przed innymi zadaniami.
# Wzajemne kolejności zadań opisuje dwuwymiarowa tablica T[N][N]. Jeżeli T[a][b] = 1 to wykonanie zadania a musi
# poprzedzać wykonanie zadania b. W przypadku gdy T[a][b] = 2 zadanie b
# musi być wykonane wcześniej, a gdy T[a][b] = 0 kolejność zadań a i b jest obojętna. Proszę zaimplementować funkcję
# tasks(T), która dla danej tablicy T, zwraca tablicę z kolejnymi numerami
# zadań do wykonania.
#
# Przykład Dla tablicy T = [ [0,2,1,1], [1,0,1,1], [2,2,0,1], [2,2,2,0] ] wynikiem
# jest tablica [1,0,2,3].
from queue import Queue


def tasks(T):
    n = len(T)
    G = T_to_G(T)
    visited = [-1] * n
    parents = [-1] * n
    sTp = []
    for i in range(n):
        if visited[i] == -1:
            DFS(G, visited, parents, i, sTp)
            sTp = sTp[::-1]

    parents, k = BFS(G, sTp[0], parents)

    return getRoad(parents, k)


def getRoad(p, k):
    r = []
    while k != -1:
        r.append(k)
        k = p[k]

    return r[::-1]


def DFS(G, visited, parents, u, sTp):
    n = len(G)
    visited[u] = 1

    for i in range(n):
        if G[u][i] > 0 and visited[i] == -1:
            parents[i] = u
            DFS(G, visited, parents, i, sTp)

    sTp.append(u)


def BFS(G, s, parents):
    n = len(G)
    Q = Queue()
    v = [-1] * n

    v[s] = 1
    Q.put(s)

    while not Q.empty():
        u = Q.get()
        v[u] = 1
        for i in range(n):
            if v[i] != 1 and G[u][i] == 1:
                parents[i] = u
                Q.put(i)

    return parents, u


def T_to_G(T):
    n = len(T)
    G = [[-1] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i != j and T[i][j] == 1:
                G[i][j] = 1
            elif i != j and T[i][j] == 2:
                G[j][i] = 1
            elif i != j and T[i][j] == 0:
                G[i][j] = 1
                G[j][i] = 1

    return G


T = [[0, 2, 1, 1], [1, 0, 1, 1], [2, 2, 0, 1], [2, 2, 2, 0]]

print(tasks(T))
