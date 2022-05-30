# Zadanie 7. (kosztowna szachownica) Dana jest szachownica o wymiarach n × n. Każde pole (i, j)
# ma koszt (liczbę ze zbioru {1, . . . , 5}) umieszczony w tablicy A (na polu A[j][i]). W lewym górnym rogu
# szachownicy stoi król, którego zadaniem jest przejsc do prawego dolnego rogu, przechodzac po polach o
# minmalnym sumarycznym koszcie. Prosze zaimplementowac funkcje kings path(A), która oblicza koszt
# sciezki króla. Funkcja powinna byc mozliwie jak najszybsza.


from queue import PriorityQueue
from math import inf


def kings_path(A, s, k):
    dp = dijkstry(A, s)

    for j in A:
        print(j)
    print()
    for i in dp:
        print(i)

    return dp[k[0]][k[1]]


def dijkstry(G, s):
    n = len(G)
    Q = PriorityQueue()

    dp = [[inf for _ in range(n)] for _ in range(n)]

    dp[s[0]][s[1]] = G[s[0]][s[1]]
    Q.put((G[s[0]][s[1]], s))
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while not Q.empty():
        _, i = Q.get()
        for m in moves:
            x, y = i[0] + m[0], i[1] + m[1]
            if if_possible(x, y, n) and dp[x][y] > dp[i[0]][i[1]] + G[x][y]:
                dp[x][y] = dp[i[0]][i[1]] + G[x][y]
                next = (x, y)
                Q.put((dp[x][y], next))

    return dp


def if_possible(i, j, n):
    if 0 <= i < n and 0 <= j < n: return True
    return False


A = [[1, 1, 4, 5, 3, 5],
     [4, 1, 4, 2, 3, 4],
     [1, 5, 1, 1, 2, 4],
     [1, 1, 1, 2, 5, 3],
     [2, 1, 3, 5, 4, 5],
     [1, 2, 4, 4, 3, 2]]

B = [[1, 100, 0, 0],
     [99, 2, 1, 0],
     [1, 2, 1, 0],
     [1, 2, 99, 2]]

C = [[4, 0, 2, 1],
     [0, 0, 2, 1],
     [1, 1, 0, 4],
     [0, 3, 0, 1]]

n = len(A)
s, k = (0, 0), (n - 1, n - 1)

print(kings_path(A, s, k))
