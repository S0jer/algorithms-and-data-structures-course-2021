# Paweł Jaśkowiec, 406165

# Funkcja BlueAndGreen na poczatku wyznacza odległoście między wierzchołkami (algorytm Floyda-Warshall'a) i zastępuje
# tablice T tablicą z najkrótszymi wartościami oraz powiekszam o zródło oraz ujście macierz T aby użyc maksymalnego przepływu
# następnie dla wierzchołków spełniających warunki zadanie, tzn rózne kolory oraz odległości wieksze niz D
# jeden kolor łączę z zrodlem, następnie je między soba oraz na koniec drugi kolor z ujsciem a nastepnie
# uruchamiam algorytm maksymalnego przepływu który zwraca rozwiazanie


from zad3testy import runtests

from zad3EK import edmonds_karp


def BlueAndGreen(T, K, D):
    T = floyd_warshall(T)  # obliczam odleglości miedzy wierzchołkami za pomoca algorytmy Floyd'a Warshall'a
    n = len(T)

    # powiekszam tablice o zrodlo oraz ujscie
    T = T + [[0] * (n + 2)] + [[0] * (n + 2)]
    for i in range(n):
        T[i] = T[i] + [0, 0]

    for i in range(n):
        if K[i] == 'B':
            for j in range(n):
                if K[j] == 'G' and T[i][j] >= D:  # wierzchołki spełniające warunki zadania łącze odpowiednio
                    T[n][i] = 1
                    T[i][j] = 1
                    T[j][n + 1] = 1
                else:  # nie spełniające warunków rodzielam
                    T[i][j] = 0

    max_flow = edmonds_karp(T, n, n + 1)  # otrzymuje wynik za pomocą maksymalnego przeplywu

    return max_flow


def floyd_warshall(G):
    n = len(G)

    inf = 100000
    dp = [[inf] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if G[i][j] != 0:
                dp[i][j] = G[i][j]
            else:
                dp[i][j] = inf

    for t in range(n):
        for u in range(n):
            for w in range(n):
                if u != w:
                    dp[u][w] = min(dp[u][w], dp[u][t] + dp[t][w])

    return dp


runtests(BlueAndGreen)
