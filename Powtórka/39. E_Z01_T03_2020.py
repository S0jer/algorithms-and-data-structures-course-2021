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
# jest spójny, acykliczny, oraz jeśli a ∈ lb to b ∈ la (graf jest nieskierowany). Nagłówek funkcji powinien
# mieć postać:

from queue import PriorityQueue
from math import inf


def best_root(L):
    n = len(L)
    r_max, result = inf, None

    for i in range(n):
        x = max(dijkstry(L, i))

        if r_max > x:
            r_max = x
            result = i

    return result


def dijkstry(G, s):
    n = len(G)
    Q = PriorityQueue()

    dp = [inf] * n

    dp[s] = 0
    Q.put((0, s))

    while not Q.empty():
        u = Q.get()

        for i in G[u[1]]:
            if dp[i] > dp[u[1]] + 1:
                dp[i] = dp[u[1]] + 1
                Q.put((dp[i], i))

    return dp


L = [[2],
     [2],
     [0, 1, 3],
     [2, 4],
     [3, 5, 6],
     [4],
     [4]]

print(best_root(L))
