

def knapsack_2(w, v, MaxW):
    n = len(w) + 1
    sumV = [0] * (len(v) + 2)

    for i in range(2, n + 1):
        sumV[i] = sumV[i - 1] + v[i - 2]

    v = [0] + v
    w = [0] + w

    M = [[0 for _ in range(sumV[len(sumV) - 1] + 1)] for _ in range(n)]

    for i in range(1, n):
        for j in range(1, sumV[len(sumV) - 1] + 1):
            if j > sumV[i]:
                M[i][j] = w[i] + M[i - 1][j - v[i]]
            else:
                M[i][j] = min(M[i - 1][j], w[i] + M[i - 1][max(0, j - v[i])])

    return recover(M, w, v, MaxW)


def recover(M, w, v, MaxW):
    i = len(M) - 1
    j = len(M[0]) - 1

    while M[i][j] > MaxW:
        j -= 1

    solution = []
    while i > 0 and j > 0:
        if M[i][j] == w[i] + M[i - 1][max(0, j - v[i])]:
            solution.append(i - 1)
            j = max(0, j - v[i])
        i -= 1
    return solution[::-1]


w = [4, 5, 12, 9, 1, 13]
v = [10, 8, 4, 5, 3, 7]
MaxW = 24

result = knapsack_2(w, v, MaxW)
print(result)
