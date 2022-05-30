# Zadanie 6. (bezpieczny przelot) Dany jest graf G = (V, E), którego wierzchołki reprezentują punkty
# nawigacyjne nad Bajtocją, a krawędzie reprezentują korytarze powietrzne między tymi punktami. Każdy
# korytarz powietrzny ei ∈ E powiązany jest z optymalnym pułapem przelotu pi ∈ N (wyrażonym w metrach).
# Przepisy dopuszczają przelot danym korytarzem jeśli pułap samolotu różni się od optymalnego najwyżej o t
# metrów. Proszę zaproponować algorytm (bez implementacji), który sprawdza czy istnieje możliwość przelotu
# z zadanego punktu x ∈ V do zadanego punktu y ∈ V w taki sposób, żeby samolot nigdy nie zmieniał pułapu.
# Algorytm powinien być poprawny i możliwie jak najszybszy. Proszę oszacować jego złożoność czasową.


def safe_flight(G, s, k, p, t):
    v = DFS_K(G, s, k, p, t)

    if v[k] == 1:
        return True

    return False


def DFS_K(G, s, k, p, t):
    n = len(G)
    v = [-1] * n

    DFSVisit_K(G, s, v, p, t)

    return v


def DFSVisit_K(G, u, v, p, t):
    v[u] = 1

    for i in G[u]:
        if v[i[0]] != 1 and p - t <= i[1] <= p + t:
            DFSVisit_K(G, i[0], v, p, t)


graph = [[(1, 15), (3, 11), (2, 12)],
         [(5, 14), (0, 15), (4, 11)],
         [(4, 10), (0, 12)],
         [(6, 15), (0, 11)],
         [(1, 11), (7, 17), (2, 10)],
         [(6, 13), (7, 18), (1, 14)],
         [(7, 14), (3, 15), (5, 13)],
         [(4, 17), (5, 18), (6, 10)]]

s, k, p, t = 0, 7, 12, 2
print(safe_flight(graph, s, k, p, t))
