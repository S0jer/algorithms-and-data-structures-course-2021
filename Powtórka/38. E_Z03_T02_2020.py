# Dany jest zbiór N zadań, gdzie niektóre zadania muszą być wykonane przed innymi zadaniami.
# Wzajemne kolejności zadań opisuje dwuwymiarowa tablica T[N][N]. Jeżeli T[a][b] = 1 to wykonanie
# zadania a musi poprzedzać wykonanie zadania b. W przypadku gdy T[a][b] = 2 zadanie b musi być wykonane
# wcześniej, a gdy T[a][b] = 0 kolejność zadań a i b jest obojętna. Proszę zaimplementować
# funkcję tasks(T), która dla danej tablicy T, zwraca tablicę z kolejnymi numerami zadań do wykonania.

from math import inf


def tasks(T):
    G = makeGraph(T)

    result = DFS_Tp(G)

    return result


def DFS_Tp(G):
    n = len(G)
    v = [-1] * n
    delete = []

    i = 0
    while i != n - 1:
        delete, v = DFSVisit_Tp(G, i, v, delete)
        while i != n - 1 and v[i] != -1:
            i += 1

    return delete[::-1]


def DFSVisit_Tp(G, u, v, delete):
    v[u] = 1
    n = len(G)
    for i in range(n):
        if v[i] != 1 and G[u][i] == 1:
            DFSVisit_Tp(G, i, v, delete)

    delete.append(u)

    return delete, v


def makeGraph(T):
    n = len(T)
    G = [[-1 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if T[i][j] == 0:
                G[i][j] = 1
                G[j][i] = 1
            elif T[i][j] == 1:
                G[i][j] = 1
            elif T[i][j] == 2:
                G[j][i] = 1

    return G


T = [[0, 2, 1, 1], [1, 0, 1, 1], [2, 2, 0, 1], [2, 2, 2, 0]]

print(tasks(T))
# [1,0,2,3]
