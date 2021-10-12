# Paweł Jaśkowiec, 406165

# Program na początku sprawdza czy w danym grafie może wystąpić cykl Eulera, tzn. sprawdza czy graf jest spójny
# poprzez sprawdzenie czy algorytm BFS odwiedza każdy wierzchołek oraz jednocześnie zlicza ilość krawędzi dla odwiedzonego
# wierzchołka i sprawdza czy stopień każdego wierzchołka jest parzysty, jeśli graf spełnia te warunki znajduję dany
# cykl Eulera używając funkcji DFSVisit która przechodząc po krawędzi usuwa ją i dzięki temu odtwarza nasz cykl Eulera
# oraz zwraca jego trasę (listę kolejno odwiedzonych punktów), w tym procesie ulega  uszkodzeniu macierz G, dlatego
# następnie funkcją repair przywracam macierz G do pierwotnego stanu dzięki tablicy road zawierającej cykl Eulera


from copy import deepcopy

import queue


def BFS(G, s):
    n = len(G)
    Q = queue.Queue()

    l = [0] * n
    v = [-1] * n

    v[s] = 1
    Q.put(s)
    w = 1

    while not Q.empty():
        u = Q.get()
        for i in range(n):
            if G[u][i] == 1:
                # liczenie stopnia każdego wierzchołka
                l[u] += 1
            if v[i] != 1 and G[u][i] == 1:
                # liczenie odwiedzonych wierzchołków
                w += 1
                v[i] = 1
                Q.put(i)

    return l, w


def euler(G):
    n = len(G)
    road = []

    l, w = BFS(G, 0)  # algorytm BFS zlicza stopnie wierzchołków oraz liczy do ilu wierzchołków dotarł

    # sprawdzam spójność
    if w != n:
        return None
    # sprawdzam WKW na istnienie cyklu Eulera (czy stopnie wierzchołków są parzyste)
    for i in l:
        if i % 2 != 0:
            return None

    u = 0

    # znajduję cykl Eulera i zapisuję w tablicy road, G ulega uszkodzeniu
    road = DFSVisit(G, u, road)

    # za pomocą tablicy road przywracam macierz G do pierwotnego stanu
    repair(road, G)

    return road


def DFSVisit(G_C, u, road):
    n = len(G_C)

    for i in range(n):
        if G_C[u][i] == 1:
            # przechodząc po wierzchołkach usuwam krawędź po której przeszedłem
            G_C[u][i] = 0
            G_C[i][u] = 0
            DFSVisit(G_C, i, road)
    # zapisuje odwiedzone wierzchołki
    road.append(u)

    return road


def repair(road, G):
    n = len(road)
    # odtwarzam pierwotny wygląd macierzy G dzięki tablicy road
    for i in range(n - 1):
        G[road[i]][road[i + 1]] = 1
        G[road[i + 1]][road[i]] = 1


### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik


G = [[0, 1, 1, 0, 0, 0],
     [1, 0, 1, 1, 0, 1],
     [1, 1, 0, 0, 1, 1],
     [0, 1, 0, 0, 0, 1],
     [0, 0, 1, 0, 0, 1],
     [0, 1, 1, 1, 1, 0]]

r = euler(G)
print(r)

GG = deepcopy(G)
cycle = euler(G)

if cycle == None:
    print("Błąd (1)!")
    exit(0)

u = cycle[0]
for v in cycle[1:]:
    if GG[u][v] == False:
        print("Błąd (2)!")
        exit(0)
    GG[u][v] = False
    GG[v][u] = False
    u = v

for i in range(len(GG)):
    for j in range(len(GG)):
        if GG[i][j] == True:
            print("Błąd (3)!")
            exit(0)

print("OK")
