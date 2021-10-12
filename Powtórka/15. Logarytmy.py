# Zadanie 4. (logarytmy) Mamy dany graf G = (V, E) z wagami w∶ E → N−{0} (dodatnie liczby naturalne).
# Chcemy znalezc scieżkę z wierzchołka u do v tak, by iloczyn wag był minimalny. Omówic rozwiązanie (bez
# implementacji)

from queue import PriorityQueue
from math import log10, inf


def logarytm(G, s):
    n = len(G)
    Q = PriorityQueue()

    dp = [inf] * n
    p = [-1] * n

    dp[s] = 0
    Q.put((0, s))

    while not Q.empty():
        floor, u = Q.get()

        for i in range(n):
            if G[u][i] != 0 and dp[i] > dp[u] + log10(G[u][i]):
                dp[i] = dp[u] + log10(G[u][i])
                Q.put((dp[i], i))
                p[i] = u

    return dp


G = [[0, 10, 100, 0, 0],
     [10, 0, 100, 10, 100],
     [100, 100, 0, 0, 1000],
     [0, 10, 0, 0, 10],
     [0, 100, 1000, 10, 0]]

print(logarytm(G, 0))
