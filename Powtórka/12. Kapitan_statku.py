# Zadanie 1. (kapitan statku, zadanie z kolokwium w 2012/13) Kapitan pewnego statku zastanawia
# się, czy może wpłynąć do portu mimo, że nastąpił odpływ. Do dyspozycji ma mapę zatoki w postaci tablicy
# M, gdzie M[y][x] to głebokość zatoki na pozycji (x, y). Jeśli jest ona większa niż pewna wartość int T
# to statek może się tam znaleźć. Początkowo statek jest na pozycji (0, 0) a port znajduje się na pozycji
# (n − 1, m − 1). Z danej pozycji statek może przepłynąć bezpośrednio jedynie na pozycję bezpośrednio obok
# (to znaczy, na pozycję, której dokładnie jedna ze współrzędnych różni się o jeden). Proszę napisać funkcję
# rozwiązującą problem kapitana.

import queue


def captain_M(M, L, s, k):
    n, s_p, k_p, cnt = len(M), 0, 0, 0

    for i in range(n):
        for j in range(n):
            if M[i][j] >= L:

                if s[0] == i and s[1] == j:
                    s_p = cnt
                if k[0] == i and k[1] == j:
                    k_p = cnt

                M[i][j] = cnt
                cnt += 1

            else:
                M[i][j] = -1

    dp = [[-1 for _ in range(cnt)] for _ in range(cnt)]

    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for a in range(n):
        for b in range(n):
            if M[a][b] != -1:
                for m in moves:
                    if if_possible(a + m[0], b + m[1], n) and M[a + m[0]][b + m[1]] != -1:
                        dp[M[a][b]][M[a + m[0]][b + m[1]]] = 1

    return BFS(dp, s_p, k_p)


def BFS(G, s, k):
    n = len(G)
    Q = queue.Queue()

    v = [-1] * n

    v[s] = 1
    Q.put(s)

    while not Q.empty():
        u = Q.get()
        for i in range(n):
            if v[i] != 1 and G[u][i] == 1:
                v[i] = 1
                Q.put(i)

    if v[k] == 1:
        return True

    return False


def captain_S(M, L, s, k):
    n, s_p, k_p, cnt = len(M), 0, 0, 0

    for i in range(n):
        for j in range(n):
            if M[i][j] >= L:

                if s[0] == i and s[1] == j:
                    s_p = cnt

                if k[0] == i and k[1] == j:
                    k_p = cnt

                M[i][j] = cnt
                cnt += 1

            else:
                M[i][j] = -1

    dp = [[] for _ in range(cnt)]

    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for a in range(n):
        for b in range(n):
            if M[a][b] != -1:
                for m in moves:
                    if if_possible(a + m[0], b + m[1], n) and M[a + m[0]][b + m[1]] != -1:
                        dp[M[a][b]].append(M[a + m[0]][b + m[1]])

    return BFS_K(dp, s_p, k_p)


def BFS_K(G, s, k):
    n = len(G)
    Q = queue.Queue()

    v = [-1] * n

    v[s] = 1
    Q.put(s)

    while not Q.empty():
        u = Q.get()
        for i in G[u]:
            if v[i] != 1:
                v[i] = 1
                Q.put(i)

    if v[k] == 1:
        return True

    return False


def if_possible(i, j, n):
    if 0 <= i and i < n and 0 <= j and j < n:
        return True
    return False


M = [[3, 1, 4, 5, 5],
     [4, 2, 3, 2, 5],
     [3, 1, 1, 1, 5],
     [3, 3, 3, 2, 2],
     [1, 1, 4, 2, 5]]

L = 3

result_m = captain_M(M, L, (0, 0), (4, 4))
print(result_m)

M = [[3, 1, 4, 5, 5],
     [4, 2, 3, 2, 5],
     [3, 1, 1, 1, 5],
     [3, 3, 3, 2, 2],
     [1, 1, 4, 2, 5]]

result_k = captain_S(M, L, (0, 0), (4, 4))
print(result_k)
