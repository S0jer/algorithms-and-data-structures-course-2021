# Sprawdza czy istnieje podciąg o sumie T

def printT(A):
    for i in A:
        print(i)

def substring_sum(A, T):
    n = len(A)
    dp = [[1] + [0] * T for _ in range(n)]
    printT(dp)

    if A[0] <= T:
        dp[0][A[0]] = 1

    for i in range(1, n):
        for j in range(1, T + 1):
            dp[i][j] = dp[i - 1][j]
            if A[i] <= j and dp[i][j] == 0:
                dp[i][j] = dp[i - 1][j - A[i]]
    printT(dp)
    if dp[n - 1][T] == 1:
        return True
    return False


A = [5, 6, 7, 3, 3, 8, 13]
T = 21
print(substring_sum(A, T))
