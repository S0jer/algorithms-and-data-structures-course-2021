from copy import deepcopy
from queue import PriorityQueue


def max_extending_path(G, s, t):
    Q = PriorityQueue()

    Q.put((0, s, [s]))

    while not Q.empty():

        u = Q.get()
        if u[1] != t:
            for i in range(len(G[u[1]])):

                if len(u[2]) == 1:
                    Q.put(((-1) * G[u[1]][i][1], G[u[1]][i][0], u[2] + [G[u[1]][i][0]]))

                else:
                    if G[u[1]][i][0] not in u[2]:
                        Q.put(((-1) * min(G[u[1]][i][1], (-1) * u[0]), G[u[1]][i][0], u[2] + [G[u[1]][i][0]]))
        else:
            return u[2]

    return []


### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik

G = [[(1, 4), (2, 3)],  # 0
     [(3, 2)],  # 1
     [(3, 5)],  # 2
     []]  # 3

s = 0
t = 3
C = 3

GG = deepcopy(G)
path = max_extending_path(GG, s, t)

print("Sciezka :", path)

if path == []:
    print("Błąd (1): Spodziewano się ścieżki!")
    exit(0)

if path[0] != s or path[-1] != t:
    print("Błąd (2): Zły początek lub koniec!")
    exit(0)

capacity = float("inf")
u = path[0]

for v in path[1:]:
    connected = False
    for (x, c) in G[u]:
        if x == v:
            capacity = min(capacity, c)
            connected = True
    if not connected:
        print("Błąd (3): Brak krawędzi ", (u, v))
        exit(0)
    u = v

print("Oczekiwana pojemność :", C)
print("Uzyskana pojemność   :", capacity)

if C != capacity:
    print("Błąd (4): Niezgodna pojemność")
else:
    print("OK")
