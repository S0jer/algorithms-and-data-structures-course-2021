# Zadanie 5. (maximin) Rozważmy ciąg (a0, . . . , an−1) liczb naturalnych. Załóżmy, że został podzielony
# na k spójnych podciągów: (a0, . . . , a`1), (a`1+1, . . . , a`2), . . . , (a`k−1+1, . . . , an−1).
# Przez wartość i-go podciągu rozumiemy sumę jego elementów a przez najgorszy podciąg rozumiemy podciąg o najmniejszej
# wartości (rozstrzygając remisy w dowolny sposób). Wartością podziału jest wartość jego najgorszego podciągu.
# Zadanie polega na znalezienie podziału ciągu (a0, . . . , an−1) o maksymalnej wartości.

from math import inf


def maximin(A, k):
    n = len(A)
    dp = [0] * k
    sums = [0] * k

    for i in range(k):
        dp[i] = i
        sums[i] = A[i]

    for i in range(k, n):
        j = k - 1
        idx = dp[j - 1] + 1
        dp[j] += 1
        sums[j] += A[i]

        while (abs(sums[j] - sums[j - 1]) >= abs(sums[j] - 2 * A[idx] - sums[j - 1])) and j > 0 and idx > -1:
            sums[j] -= A[idx]
            sums[j - 1] += A[idx]
            dp[j - 1] += 1
            j -= 1
            idx = dp[j - 1] + 1

    print(dp)


def maximin_v2(A, k):
    n = len(A)
    dp = [[inf for _ in range(k + 1)] for _ in range(n)]
    sums = [0] * n

    for i in range(n):
        sums[i] = sums[i - 1] + A[i]

    for t in range(1, k + 1):
        for i in range(n):
            for o in range(i):
                dp[i][t] = min(dp[i - o][t - 1], abs(sums[i] - sums[o]))

    for i in dp:
        print(i)


if __name__ == '__main__':

    A = [1, 2, 3, 2, 4, 6, 11, 1, 12, 13, 2, 3, 0]
    B = [12, 0, 0, 12, 0, 0, 12, 0, 0, 12, 0, 0]
    C = [100, 99, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    k = 4

    maximin_v2(A, k)

    # maximin(A, k - 1)
    # maximin(B, k - 1)
    # maximin(C, k - 1)


