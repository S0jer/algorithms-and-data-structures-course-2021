# Pewna kraina składa się z wysp pomiędzy którymi istnieją połączenia lotnicze, promowe oraz mosty.
# Pomiędzy dwoma wyspami istnieje co najwyżej jeden rodzaj połączenia. Koszt przelotu z wyspy
# na wyspę wynosi 8B, koszt przeprawy promowej wynosi 5B, za przejście mostem trzeba wnieść
# opłatę 1B. Poszukujemy trasy z wyspy A na wyspę B, która na kolejnych wyspach zmienia środek
# transportu na inny oraz minimalizuje koszt podróży.
# Dana jest tablica G, określająca koszt połączeń pomiędzy wyspami. Wartość 0 w macierzy
# oznacza brak bezpośredniego połączenia. Proszę zaimplementować funkcję islands( G, A, B )
# zwracającą minimalny koszt podróży z wyspy A na wyspę B. Jeżeli trasa spełniająca warunki zadania
# nie istnieje, funkcja powinna zwrócić wartość None.

from math import inf


def islands(G, A, B):
    dp, p = dijkstra_M(G, A)

    if dp[B][1] == inf:
        return False

    result = dp[B][1]
    road = get_road(p, A, B)

    return road, result


def dijkstra_M(G, s):
    n = len(G)

    dp = [(0, inf) for _ in range(n)]
    p = [-1] * n
    visited = [False] * n

    dp[s] = (0, 0)

    for i in range(n):

        u = min_distance(dp, visited)
        visited[u] = True

        for j in range(n):
            if dp[j][1] > dp[u][1] + G[u][j] and G[u][j] != 0 and visited[j] is False and dp[u][0] != G[u][j]:
                dp[j] = (G[u][j], dp[u][1] + G[u][j])
                p[j] = u

    return dp, p


def min_distance(dp, visited):
    min_w, min_idx, n = inf, 0, len(dp)

    for i in range(n):
        if dp[i][1] < min_w and visited[i] is False:
            min_w = dp[i][1]
            min_idx = i

    return min_idx


def get_road(p, A, B):
    road = [B]
    position = B
    while position != A:
        position = p[position]
        road.append(position)

    return road[::-1]


G1 = [[0, 5, 1, 8, 0, 0, 0],
      [5, 0, 0, 1, 0, 8, 0],
      [1, 0, 0, 8, 0, 0, 8],
      [8, 1, 8, 0, 5, 0, 1],
      [0, 0, 0, 5, 0, 1, 0],
      [0, 8, 0, 0, 1, 0, 5],
      [0, 0, 8, 1, 0, 5, 0]]
print(islands(G1, 5, 2))
# 13
