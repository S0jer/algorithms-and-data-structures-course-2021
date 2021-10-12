# Dany jest graf skierowany G = (V,E) w reprezentacji macierzowej (bez wag). Proszę zaimplementować algorytm,
# który oblicza domknięcie przechodnie grafu G (domknięcie przechodnie grafu G to takie graf H,
# że w H mamy krawędź z u do v wtedy i tylko wtedy gdy w G jest ścieżka skierowana z u do v).



def floyd_warshall(G):
    n = len(G)

    reach = [i[:] for i in G]

    for t in range(n):
        for u in range(n):
            for w in range(n):
                reach[u][w] = reach[u][w] or (reach[u][t] and reach[t][w])

    for i in reach:
        print(i)

    return reach



graph = [[1, 1, 1, 0],
         [0, 1, 1, 0],
         [1, 0, 1, 1],
         [0, 0, 0, 1]]

floyd_warshall(graph)
