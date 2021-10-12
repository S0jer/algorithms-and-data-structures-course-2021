# Paweł Jaśkowiec, 406165

# Przechodzę BFS'em i znajduję ile jest najkrótszych ścieżek oraz trasę danej najkrótszej, jeśli znajdzie
# mi więcej niż jedną najkrótszą trasę to zwracam None,  jeśli znajdzie mi jedną najkrótszą to sprawdzam które krawędzie mogę
# usunąć nie rozspujniając grafu, jeśli mogę usunąć to zapisuję do tablicy które moge usunąć i sprawdzam kolejne

# Mam problem z testami bo wypisuję w innej kolejności ale odpowiedzi się zgadzają

from zad2testy import runtests

from queue import Queue


def enlarge(G, s, t):
    n = len(G)
    deleted = []
    # znajduję ile najkrótszych ścieżek idzie do punktu docelowego oraz jaką trase idzie jeden z nich
    arrivals, ile, answer = BFS(G, s, t)

    if len(arrivals) > 1:
        return None

    # sprawdzam które krawędzie z najkrótszej trasy mogę usunąć niszcząc tą trasę oraz nie rozspujniając grafu
    # dzieki uzyciu BFS'a
    for i in range(len(answer) - 1):

        G[answer[i]].remove(answer[i + 1])
        G[answer[i + 1]].remove(answer[i])
        print()
        arrivals, ile, xyz = BFS(G, t, s)

        if ile == n:
            deleted.append((answer[i + 1], answer[i]))

        G[answer[i]].append(answer[i + 1])
        G[answer[i + 1]].append(answer[i])

    if len(deleted) > 0:
        return deleted

    return None


def BFS(G, s, t):
    n = len(G)
    Q = Queue()

    answer = [t] * n
    ile = 0
    min_w = 1000
    arrivals = []
    waves = [0] * n
    v = [-1] * n
    v_parent = [-1] * n

    v[s] = 1
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        ile += 1
        for i in G[u]:

            waves[i] = waves[u] + 1
            if v[i] != 1:
                v[i] = 1
                v_parent[i] = u
                Q.put(i)
            x = t
            # jesli znajde inna krótszą od obecnej to podmieniam
            if i == t and waves[i] < min_w:
                answer = [t]
                min_w = waves[i]
                while v_parent[x] != -1 and x != s:
                    answer.append(v_parent[x])
                    x = v_parent[x]

                arrivals = [v_parent[i]]
            # jeśli jest wiecej niz jedna najkrotsza to dodaje wierzcholek z ktorego idzie
            elif i == t and waves[i] == min_w:
                answer = [t]
                while v_parent[x] != -1 and x != s:
                    answer.append(v_parent[x])
                    x = v_parent[x]

                arrivals.append(v_parent[i])

    return arrivals, ile, answer


runtests(enlarge)
