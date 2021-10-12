# Zadanie 6. (wydawanie monet) Mamy daną tablicę z nominałami monet stosowanych w pewnym dziwnym kraju, oraz kwotę T.
# Proszę podać algorytm, który oblicza minimalną ilość monet potrzebną do wydania
# kwoty T (algorytm zachłanny, wydający najpierw największą monetę, nie działa: dla monet 1, 5, 8 wyda
# kwotę 15 jako 8 + 5 + 1 + 1 zamiast 5 + 5 + 5).

from math import inf


def printT(A):
    for i in A:
        print(i)


def coins(A, T):
    n = len(A)
    dp = [[inf] + [inf] * T for _ in range(n)]

    x = 1
    while A[0] * x <= T:
        dp[0][A[0] * x] = x
        x += 1

    for i in range(1, n):
        for j in range(1, T + 1):
            if dp[i - 1][j] != 0:
                dp[i][j] = dp[i - 1][j]

            x = j
            s = 0
            result = inf

            while x >= A[i]:
                x -= A[i]
                s += 1
                if dp[i][x] > 0:
                    result = min(s + dp[i][x], result)
            if x > 0 and dp[i][x] != 0:
                result = min(s + dp[i][x], result)
            elif x == 0:
                result = min(s, result)

            dp[i][j] = min(result, dp[i][j])

    result = T

    for i in range(n):
        if dp[i][T] < result and dp[i][T] > 0:
            result = dp[i][T]

    print(result)


A = [2, 3, 8]
T = 15
coins(A, T)
