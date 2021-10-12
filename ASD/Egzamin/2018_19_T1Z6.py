# Bob i praca


def impatientbob(T, k):
    n = len(T)
    inf = 100000
    T.sort(key=lambda T: T[1])

    dp = [[inf] * (k + 1) for _ in range(n)]

    for i in range(n):
        dp[i][1] = 0

    for i in range(n):
        for j in range(i):
            for z in range(k):
                if T[i][0] >= T[j][1]:
                    dp[i][z + 1] = min(dp[j][z] + abs(T[j][1] - T[i][0]), dp[i][z + 1])

    best = inf
    for i in range(n):
        best = min(best, dp[i][k])

    if best == inf:
        return None
    return best


Jobs = [(0, 1), (2, 4), (0, 5), (3, 6), (5, 7), (2, 9), (4, 10), (8, 11), (10, 12)]
k = 4

print(impatientbob(Jobs, k))
