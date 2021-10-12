# Paweł Jaśkowiec, 406165
#
# Algorytm wykonuje podział zbioru krawędzi na podzbiory A oraz B za pomocą algorytmu Kruskala, oraz dopiera odpowiednia krawędzie szukając


from copy import deepcopy


def min_cycle(G):
    n = len(G)
    E, A, B = [], [], []

    for i in range(n):
        for j in range(n):
            if G[i][j] != -1:
                E.append(((i, j), G[i][j]))
                if G[i][j] == G[j][i]:
                    G[i][j] = -1
                    G[j][i] = -1
                else:
                    G[i][j] = -1

    E.sort(key=lambda E: E[1])

    m = len(E)
    v_p = [i for i in range(m)]
    rank = [0] * m

    for i in range(m):
        if find(E[i][0][0], v_p) != find(E[i][0][1], v_p):
            union(E[i][0][0], E[i][0][1], v_p, rank)
            A.append(E[i])
        else:
            B.append(E[i])

    b = len(B)
    a = len(A)

    print(A)
    print(B)

    road_min = []
    cost_min = 100000

    for i in range(b):

        cost = B[i][1]
        start = B[i][0][0]
        end = B[i][0][1]
        road = [end]
        used_a = [-1] * a
        used_b = [-1] * b
        used_b[i] = 1

        while start != end:

            next_step = 0
            travel_min = 10000
            c, u_a, u_b = 0, -1, -1

            for j in range(a - 1, -1, -1):

                if A[j][1] <= travel_min and A[j][0][0] == end and used_a[j] == -1:
                    travel_min = A[j][1]
                    next_step = A[j][0][1]
                    c = 1
                    u_a = j

                elif A[j][1] <= travel_min and A[j][0][1] == end and used_a[j] == -1:
                    travel_min = A[j][1]
                    next_step = A[j][0][0]
                    c = 1
                    u_a = j

                if j < len(B) and B[j][1] <= travel_min and B[j][0][0] == end and used_b[j] == -1:
                    travel_min = B[j][1]
                    next_step = B[j][0][1]
                    c = 1
                    u_b = j
                elif j < len(B) and B[j][1] <= travel_min and B[j][0][1] == end and used_b[j] == -1:
                    travel_min = B[j][1]
                    next_step = B[j][0][0]
                    c = 1
                    u_b = j

            if c == 0:
                break

            road.append(next_step)
            cost += travel_min

            if u_a != -1 and u_a > u_b:
                used_a[u_a] = 1
            if u_b != -1 and u_a < u_b:
                used_b[u_b] = 1

            end = next_step

        if cost < cost_min:
            cost_min = cost
            road_min = deepcopy(road)
    print(road_min, cost_min)

    return road_min


def union(x, y, v_p, rank):
    x = find(x, v_p)
    y = find(y, v_p)

    if x == y: return 1
    if rank[x] > rank[y]:
        v_p[y] = x
    else:
        v_p[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1


def find(x, v_p):
    if x != v_p[x]:
        v_p[x] = find(v_p[x], v_p)
    return v_p[x]


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
