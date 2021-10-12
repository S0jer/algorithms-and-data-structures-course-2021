

def zbigniew(A):
    n = len(A)

    dp =[[0]*n for _ in range(n)]


    for a in range(A[0] + 1):
        dp[0][a] = 1


    for i in range(n):
        k = A[0]
        for j in range(n):
            for z in range(max(k - j + A[j], n)):
                dp[i][j] = min(dp[i])
