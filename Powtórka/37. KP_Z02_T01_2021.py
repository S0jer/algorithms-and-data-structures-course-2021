from zad3testy import runtests
from math import inf


def iamlate(T, V, q, l):
    result, n = inf, len(T)
    dp = [[[inf, 0, []]] for _ in range(n + 1)]
    T, V = [0] + T, [0] + V
    dp[0][0][0], dp[0][0][1] = 0, V[0]

    for i in range(n + 1):
        for z in range(len(dp[i])):
            j = i + 1
            while j < n + 1 and abs(T[j] - T[i]) <= dp[i][z][1]:
                if dp[j][0][0] > dp[i][z][0] + 1:
                    dp[j][0][0] = dp[i][z][0] + 1
                    dp[j][0][1] = min(dp[i][z][1] - abs(T[j] - T[i]) + V[j], q)
                    dp[j][0][2] = dp[i][z][2] + [j - 1]

                elif min(dp[i][z][1] - abs(T[j] - T[i]) + V[j], q) > dp[j][len(dp[j]) - 1][1]:
                    dp[j].append(
                        [dp[i][z][0] + 1, min(dp[i][z][1] - abs(T[j] - T[i]) + V[j], q), dp[i][z][2] + [j - 1]])
                j += 1
            if dp[i][z][1] + T[i] >= l:
                break

    min_len, result = inf, []
    for a in range(len(dp)):
        for b in range(len(dp[a])):
            if dp[a][b][1] + T[a] >= l and min_len > len(dp[a][b][2]):
                result = dp[a][b][2]
                min_len = len(dp[a][b][2])

    return result


runtests(iamlate)
