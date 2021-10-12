# Zadanie 5
# Dostajemy tablicę (M x N) wypełnioną wartościami. Mamy za zadanie znaleźć najdłuższą ścieżkę w tej tablicy (możemy
# przechodzić na pola sąsiadujące krawędziami), o rosnących wartościach (to znaczy, że z pola o wartości 3, mogę przejść
# na pola o wartości większej bądź równej 4). Na początku wprowadzimy pewne ułatwienie:
# Mamy dany punkt początkowy.


def lroad(A):
    m = len(A)
    n = len(A[0])

    L = [0] * (n * m)
    dp = [[0] * n for _ in range(m)]
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    idx = 0
    for i in range(m):
        for j in range(n):
            L[idx] = (A[i][j], (i, j))
            idx += 1

    L.sort(key=lambda A: A[0])

    mini = L[0][0]
    for i in range(m):
        for j in range(n):
            if A[i][j] == mini:
                dp[i][j] = 1

    for i in range(m * n):
        for x in moves:
            if if_possible(L[i][1][0] + x[0], L[i][1][1] + x[1], m, n) and A[L[i][1][0] + x[0]][L[i][1][1] + x[1]] > \
                    A[L[i][1][0]][L[i][1][1]]:
                dp[L[i][1][0] + x[0]][L[i][1][1] + x[1]] = dp[L[i][1][0]][L[i][1][1]] + 1
    for i in dp:
        print(i)


def if_possible(x, y, m, n):
    if 0 <= x and x < m and 0 <= y and y < n: return True
    return False


A = [[1, 2, 3, 4, 0, 0, 0],
     [0, 7, 6, 5, 0, 0, 0],
     [0, 8, 0, 0, 0, 0, 0],
     [0, 9, 13, 15, 70, 5, 14]]

lroad(A)
