# Zadanie 4
# Dostajemy tablicę (M x N) wypełnioną wartościami(kosztem wejścia). Mamy znaleźć minimalny koszt potrzebny do
# dostania się z pozycji [0][0] do [M-1][N-1]
# Zakładamy, że:
# 1. Możemy poruszać się tylko w bok i w dół
# 2. Wszystkie koszty są dodatnie


def road(A):
    n = len(A)
    m = len(A[0])
    dp = [[0 for _ in range(m)] for _ in range(n)]

    for a in range(m):
        dp[0][a] = dp[0][a - 1] + A[0][a]
    for b in range(n):
        dp[b][0] = dp[b - 1][0] + A[b][0]

    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = min(dp[i - 1][j] + A[i][j], dp[i][j - 1] + A[i][j])

    return dp[n - 1][m - 1]


if __name__ == '__main__':
    A = [[1, 2, 3, 4, 0, 0, 0],
         [0, 7, 6, 5, 0, 0, 0],
         [0, 8, 0, 0, 0, 0, 0],
         [0, 9, 13, 15, 70, 5, 14]]

    print(road(A))
