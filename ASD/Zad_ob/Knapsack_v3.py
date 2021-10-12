def printT(F):
    for i in range(len(F)):
        for j in range(len(F[i])):
            print(F[i][j], end=" ")
        print("\n")


def knapsack(W, V, MaxW):
    n = len(V)
    mxs = sum(V)
    dp = [[1000] * (mxs + 1) for _ in range(n)]

    dp[0][V[0]] = W[0]

    sumt = [0] * n

    for i in range(n):
        sumt[i] = sumt[i - 1] + V[i]

    for i in range(1, n):
        for s in range(1, sumt[i] + 1):
            dp[i][s] = dp[i - 1][s]
            if V[i] <= s:
                dp[i][s] = min(dp[i - 1][s], dp[i - 1][s - V[i]] + W[i])

    printT(dp)
    result = mxs
    while dp[n - 1][result] > MaxW:
        result -= 1

    return result


W = [4, 5, 12, 9, 1, 13]
V = [10, 8, 4, 5, 3, 7]
MaxW = 20

result = knapsack(W, V, MaxW)
print(result)
