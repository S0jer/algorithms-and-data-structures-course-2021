# Pewna kraina składa się z wysp pomiędzy którymi istnieją połączenia lotnicze, promowe oraz mosty.
# Pomiędzy dwoma wyspami istnieje co najwyżej jeden rodzaj połączenia. Koszt przelotu z wyspy
# na wyspę wynosi 8B, koszt przeprawy promowej wynosi 5B, za przejście mostem trzeba wnieść
# opłatę 1B. Poszukujemy trasy z wyspy A na wyspę B, która na kolejnych wyspach zmienia środek
# transportu na inny oraz minimalizuje koszt podróży.
# Dana jest tablica G, określająca koszt połączeń pomiędzy wyspami. Wartość 0 w macierzy
# oznacza brak bezpośredniego połączenia. Proszę zaimplementować funkcję islands( G, A, B )
# zwracającą minimalny koszt podróży z wyspy A na wyspę B. Jeżeli trasa spełniająca warunki zadania
# nie istnieje, funkcja powinna zwrócić wartość None


from math import inf


def islands(G, A, B):
    n = len(G)

    dp = [[inf for _ in range(3)] for _ in range(n)]
    p = [[-1 for _ in range(3)] for _ in range(n)]
    visited = [False] * n

    for a in range(3):
        dp[A][a] = 0

    for i in range(n):

        u = min_distance(dp, visited)
        visited[u] = True

        for j in range(n):
            for z in range(3):

                if dp[j][0] > dp[u][z] + G[u][j] and G[u][j] != 0 and G[u][j] == 1 and z != 0 and visited[j] is False:
                    dp[j][0] = dp[u][z] + G[u][j]
                    p[j][0] = u

                if dp[j][1] > dp[u][z] + G[u][j] and G[u][j] != 0 and G[u][j] == 5 and z != 1 and visited[j] is False:
                    dp[j][1] = dp[u][z] + G[u][j]
                    p[j][1] = u

                if dp[j][2] > dp[u][z] + G[u][j] and G[u][j] != 0 and G[u][j] == 8 and z != 2 and visited[j] is False:
                    dp[j][2] = dp[u][z] + G[u][j]
                    p[j][2] = u

    cost = min(dp[B][0], dp[B][1], dp[B][2])
    road = recover(G, dp, p, A, B)
    print(road)

    return cost


def recover(G, dp, p, A, B):
    cost = min(dp[B][0], dp[B][1], dp[B][2])
    road = []

    while cost > 0:
        for i in range(3):
            if dp[B][i] == cost:
                road.append(B)
                cost -= G[p[B][i]][B]
                B = p[B][i]
                break
    road.append(A)

    return road[::-1]


def min_distance(dp, visited):
    min_w, min_idx, n = inf, 0, len(dp)

    for i in range(n):

        if dp[i][0] < min_w and visited[i] is False:
            min_w = dp[i][0]
            min_idx = i

        if dp[i][1] < min_w and visited[i] is False:
            min_w = dp[i][1]
            min_idx = i

        if dp[i][2] < min_w and visited[i] is False:
            min_w = dp[i][2]
            min_idx = i

    return min_idx


G1 = [[0, 5, 1, 8, 0, 0, 0],
      [5, 0, 0, 1, 0, 8, 0],
      [1, 0, 0, 8, 0, 0, 8],
      [8, 1, 8, 0, 5, 0, 1],
      [0, 0, 0, 5, 0, 1, 0],
      [0, 8, 0, 0, 1, 0, 5],
      [0, 0, 8, 1, 0, 5, 0]]

G2 = [[0, 8, 0, 0, 0, 8],
      [8, 0, 5, 0, 5, 0],
      [0, 5, 0, 8, 0, 0],
      [0, 0, 8, 0, 1, 0],
      [0, 5, 0, 1, 0, 1],
      [8, 0, 0, 0, 1, 0]]

print(islands(G2, 0, 3))
