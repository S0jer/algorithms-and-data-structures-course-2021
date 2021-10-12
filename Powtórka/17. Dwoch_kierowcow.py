# Zadanie 6. (dwóch kierowców) Dana jest mapa kraju w postaci grafu G = (V, E), gdzie wierzchołki to
# miasta a krawędzie to drogi łączące miasta. Dla każdej drogi znana jest jej długość (wyrażona w kilometrach 1
# jako liczba naturalna). Alicja i Bob prowadzą (na zmianę) autobus z miasta x ∈ V do miasta y ∈ V , zamieniając
# się za kierownicą w każdym kolejnym mieście. Alicja wybiera trasę oraz decyduje, kto prowadzi pierwszy.
# Proszę zapropnować algorytm, który wskazuje taką trasę (oraz osobę, która ma prowadzić pierwsza), żeby
# Alicja przejechała jak najmniej kilometrów. Algorytm powinien być jak najszybszy (ale przede wszystkim poprawny).


from queue import PriorityQueue
from math import inf


def alice_bob(G, X, Y):
    dp_1, p_1 = dijkstry(G, X, 1)
    dp_2, p_2 = dijkstry(G, X, -1)

    print(dp_1)
    print(dp_2)
    if dp_1[Y] > dp_2[Y]:
        result = dp_2[Y]
        road = get_road(p_2, X, Y)
    else:
        result = dp_1[Y]
        road = get_road(p_1, X, Y)

    return result, road


def dijkstry(G, s, check):
    n = len(G)
    Q = PriorityQueue()

    dp = [inf] * n
    v = [-1] * n
    p = [-1] * n

    dp[s] = 0
    Q.put((0, s, check))

    while not Q.empty():
        u = Q.get()
        v[u[1]] = 1

        for i in range(n):
            if dp[i] > dp[u[1]] + G[u[1]][i] and G[u[1]][i] != -1 and u[2] == 1 and v[i] == -1:
                dp[i] = dp[u[1]] + G[u[1]][i]
                Q.put((dp[i], i, u[2] * -1))
                p[i] = u[1]

            elif dp[i] > dp[u[1]] and G[u[1]][i] != -1 and u[2] == -1 and v[i] == -1:
                dp[i] = dp[u[1]]
                Q.put((dp[i], i, u[2] * -1))
                p[i] = u[1]

    return dp, p


def get_road(v_parents, s, t):
    road = [t]
    curr = t
    while curr != s:
        curr = v_parents[curr]
        road.append(curr)

    return road[::-1]


G_1 = [[-1, 4, 3, 3, -1],
       [4, -1, 7, -1, -1],
       [3, 7, -1, 4, 2],
       [3, -1, 4, -1, 5],
       [-1, -1, 2, 5, -1]]

G_2 = [[-1, 2, -1, -1, -1, -1, -1, -1, 5],
       [-1, -1, 1, -1, -1, -1, -1, -1, -1],
       [-1, -1, -1, 3, -1, -1, 1, -1, -1],
       [-1, -1, -1, -1, 1, -1, -1, -1, -1],
       [-1, -1, -1, -1, -1, 4, -1, -1, -1],
       [-1, -1, -1, -1, -1, -1, -1, -1, -1],
       [-1, -1, -1, -1, -1, 1, -1, -1, -1],
       [-1, -1, -1, -1, -1, -1, 1, -1, -1],
       [-1, -1, -1, -1, -1, -1, -1, 4, -1]]

result, road = alice_bob(G_2, 0, 6)
print(result, road)
