# Paweł Jaśkowiec, 406165


# Algorytm wykorzystuje algorytm dijkstry aby znaleźć najkrótszą drogę z wierzchołka i do wierzchołka j usuwając przy tym
# krawędź bezpośrednio łączącą dane wierzchołki, jeśli znajdziemy taką ścieżkę, dodajemy krawędź łączącą wierzchołki i w ten
# sposób otrzymujemy cykl o jak najmniejszej sumie zawierający wierzchołki i oraz j, wykonując algorytm dijkstry dla każdej
# usuniętej krawędzi rozważymy wszystkie możliwe cykle oraz otrzymamy szukany najkrótszy cykl.


from copy import deepcopy

from queue import PriorityQueue


def min_cycle(G):
    n = len(G)

    road_min = []
    cost_min = 100000

    x = -1
    # szukam wszystkim krawędzi
    for i in range(n):
        for j in range(n - 1, x, -1):
            if G[i][j] != -1:
                road = []
                add = G[i][j]

                # usuwam krawędź i szukam najkrótszej ścieżki między i oraz j

                G[i][j] = -1
                G[j][i] = -1

                Q = PriorityQueue()

                d = [100000] * n
                p = [-1] * n

                d[i] = 0
                Q.put((0, i))

                while not Q.empty():
                    u = Q.get()[1]

                    for k in range(n):
                        if d[k] > d[u] + G[u][k] and G[u][k] != -1:
                            Q.put((G[u][k], k))
                            d[k] = d[u] + G[u][k]
                            p[k] = u

                # licze koszt cyklu oraz wyznaczam wierzchołki należące do cyklu dzięki tablicy parentów
                cost = d[j] + add
                road = get_road(road, p, i, j)

                if cost < cost_min:
                    cost_min = cost
                    road_min = deepcopy(road)

                # przywracam krawędź
                G[i][j] = add
                G[j][i] = add
        x += 1

    return road_min


# odczytuje droge z tablicy parentow
def get_road(road, p, i, j):
    road.append(j)
    while j != i:
        road.append(p[j])
        j = p[j]

    return road


### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik

G = [[-1, 2, -1, -1, 1],
     [2, -1, 4, 1, -1],
     [-1, 4, -1, 5, -1],
     [-1, 1, 5, -1, 3],
     [1, -1, -1, 3, -1]]

LEN = 7

GG = deepcopy(G)
cycle = min_cycle(GG)

print("Cykl :", cycle)

if cycle == []:
    print("Błąd (1): Spodziewano się cyklu!")
    exit(0)

L = 0
u = cycle[0]
for v in cycle[1:] + [u]:
    if G[u][v] == -1:
        print("Błąd (2): To nie cykl! Brak krawędzi ", (u, v))
        exit(0)
    L += G[u][v]
    u = v

print("Oczekiwana długość :", LEN)
print("Uzyskana długość   :", L)

if L != LEN:
    print("Błąd (3): Niezgodna długość")
else:
    print("OK")
