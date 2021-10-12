# Dany jest graf skierowany G = (V,E) oraz funkcja opisująca pojemności jego krawędzi c: E -> N.
# Proszę zaimplementować funkcję max_extending_path, która dostaje na wejściu G, c, oraz
# wierzchołki s i t i znajduje ścieżkę skierowaną z s do t o maksymalnej przepustowości
# (czyli minimalna przepustowość krawędzi na ścieżce powinna być maksymalna).


from queue import PriorityQueue


def max_extending_path(G, C, s, t):
    n = len(G)
    Q = PriorityQueue()

    Q.put((C[s][s], s, [s]))

    while not Q.empty():
        u = Q.get()

        if u[1] != t:
            for i in range(n):

                if len(u[2]) == 1 and G[u[1]][i] >= 1 and u[1] != i:
                    Q.put(((-1) * C[u[1]][i], i, u[2] + [i]))

                elif G[u[1]][i] >= 1 and u[1] != i:
                    Q.put(((-1) * min(C[u[1]][i], (-1) * u[0]), i, u[2] + [i]))
        else:
            return u[2], u[0] * (-1)


G = [[1, 1, 0, 0, 0, 0, 0],
     [0, 1, 1, 1, 1, 0, 0],
     [0, 0, 1, 0, 0, 1, 0],
     [0, 0, 0, 1, 0, 0, 1],
     [0, 0, 0, 0, 1, 0, 1],
     [0, 0, 0, 1, 0, 1, 0],
     [0, 0, 0, 0, 1, 0, 1]]

C = [[0, 5, 0, 0, 0, 0, 0],
     [0, 0, 5, 3, 6, 0, 0],
     [0, 0, 0, 0, 0, 5, 0],
     [0, 0, 0, 0, 0, 0, 4],
     [0, 0, 0, 0, 0, 0, 3],
     [0, 0, 0, 4, 0, 0, 0],
     [0, 0, 0, 0, 4, 0, 0]]

print(max_extending_path(G, C, 0, 6))
