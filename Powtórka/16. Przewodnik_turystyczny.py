# Zadanie 5. (problem przewodnika turystycznego) Przewodnik chce przewieźć grupę K turystów z
# miasta A do miasta B. Po drodze jest jednak wiele innych miast i między różnymi miastami jeżdzą autobusy o
# różnej pojemności. Mamy daną listę trójek postaci (x, y, c), gdzie x i y to miasta między którymi bezpośrednio
# jeździ autobus o pojemności c pasażerów.
# Przewodnik musi wyznaczyć wspólną trasę dla wszystkich tursytów i musi ich podzielić na grupki tak,
# żeby każda grupka mogła przebyć trasę bez rodzielania się. Proszę podać algorytm, który oblicza na ile
# (najmniej) grupek przewodnik musi podzielić turystów (i jaką trasą powinni się poruszać), źeby wszyscy
# dostali się z A do B.

from math import inf
from queue import PriorityQueue


def guide(G, A, B):
    n = 0

    for i in range(len(G)):
        n = max(G[i][0], G[i][1], n)
    n += 1

    graph = [[-1 for _ in range(n)] for _ in range(n)]

    for j in range(len(G)):
        graph[G[j][0]][G[j][1]] = G[j][2]
        graph[G[j][1]][G[j][0]] = G[j][2]

    dp, parents = dijkstry(graph, A)
    print(dp)

    road = get_road(parents, A, B)

    return dp[B], road


def dijkstry(G, s):
    n = len(G)
    Q = PriorityQueue()

    dp = [-inf] * n
    p = [-1] * n

    dp[s] = inf
    Q.put((0, s))

    while not Q.empty():
        _, u = Q.get()

        for i in range(n):
            if dp[i] < min(dp[u], G[u][i]) and G[u][i] != -1:
                dp[i] = min(dp[u], G[u][i])
                Q.put((-1 * dp[i], i))
                p[i] = u

    return dp, p


def get_road(v_parents, s, t):
    road = [t]
    curr = t
    while curr != s:
        curr = v_parents[curr]
        road.append(curr)

    return road[::-1]


G = [(0, 1, 15), (0, 2, 7), (0, 3, 12), (1, 5, 8), (5, 6, 9), (3, 5, 10), (3, 4, 11), (4, 6, 15), (2, 4, 9)]
result, road = guide(G, 0, 6)

print(result, road)
