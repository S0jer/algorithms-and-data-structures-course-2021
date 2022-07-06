# Każdy nieskierowany, spójny i acyckliczny graf G = (V, E) możemy traktować jako drzewo. Korzeniem tego drzewa
# może być dowolny wierzchołek v ∈ V . Napisz funkcję best root(L), która
# przyjmuje nieskierowany, spójny i acyckliczny graf G (reprezentowany w postaci listy sąsiedztwa) i
# wybiera taki jego wierzchołek, by wysokość zakorzenionego w tym wierzchołku drzewa była możliwie najmniejsza.
# Jeśli kilka wierzchołków spełnia warunki zadania, funkcja może zwrócić dowolny z
# nich. Wysokość drzewa definiujemy jako liczbę krawędzi od korzenia do najdalszego liścia. Uzasadnij
# poprawność zaproponowanego algorytmu i oszacuj jego złożoność obliczeniową.
# Funkcja best root(L) powinna zwrócić numer wierzchołka wybranego jako korzeń. Wierzchołki
# numerujemy od 0. Argumentem best root(L) jest lista postaci:
# L = [l0,l1, . . . ,ln−1],
# gdzie li to lista zawierająca numery wierzchołków będących sąsiadami i−tego wierzchołka. Można
# przyjąć (bez weryfikacji), że lista opisuje graf spełniający warunki zadania. W szczególności, graf
# jest spójny, acykliczny, oraz jeśli a ∈ lb to b ∈ la (graf jest nieskierowany). N


from queue import Queue
from math import inf


def best_root(L):
    n = len(L)
    b_root = 0
    max_t = inf

    for i in range(n):
        t = BFS(L, i)
        if max_t > t:
            max_t = t
            b_root = i

    return b_root


def BFS(G, s):
    n = len(G)
    Q = Queue()
    dp = [inf] * n
    v = [-1] * n

    dp[s] = 0
    Q.put(s)

    while not Q.empty():
        u = Q.get()
        v[u] = 1

        for e in G[u]:
            if v[e] == -1:
                dp[e] = dp[u] + 1
                Q.put(e)

    return max(dp)


L = [[2],
     [2],
     [0, 1, 3],
     [2, 4],
     [3, 5, 6],
     [4],
     [4]]

print(best_root(L))
