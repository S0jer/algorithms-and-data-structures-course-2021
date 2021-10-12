# Dany jest graf nieskierowany G = (V,E) z ważonymi krawędziami (w: E -> N). Proszę zaproponować jak najszybszy
# algorytm, który znajduje ścieżkę z danego wierzchołka s do danego wierzchołka t taką, że:
# Każda kolejne krawędź ma mniejszą wagę niż poprzednia
# Spośród ścieżek spełniających powyższy warunek, znaleziona ma najmniejszą sumę wa

from queue import PriorityQueue


def dijkstry(G, s, t):
    n = len(G)
    Q = PriorityQueue()


    road = [s]
    Q.put((0, s, road))

    while not Q.empty():
        u = Q.get()

        if u[1] != t:
            for i in range(n):

                if G[u[1]][i] != 0 and G[u[2][len(u[2]) - 2]][u[1]] > G[u[1]][i] and len(u[2]) > 1:
                    Q.put((u[0] + G[u[1]][i], i, u[2] + [i]))

                elif G[u[1]][i] != 0 and len(u[2]) == 1:
                    Q.put((u[0] + G[u[1]][i], i, u[2] + [i]))

        else:
            return u[2], u[0]


G2 = [[0, 1, 5, 0, 0, 0],
      [1, 0, 5, 7, 8, 0],
      [5, 5, 0, 0, 3, 2],
      [0, 7, 0, 0, 1, 0],
      [0, 8, 3, 1, 0, 0],
      [0, 0, 2, 0, 0, 0]]

print(dijkstry(G2, 4, 5))
