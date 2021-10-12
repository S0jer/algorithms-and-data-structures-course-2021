

def knapsack(W, P, MaxW):
    n = len(W)
    F = [None] * n

    for i in range(n):
        F[i] = [0] * (MaxW + 1)

    for w in range(W[0], MaxW + 1):
        F[0][w] = P[0]

    for i in range(1, n):
        for w in range(1, MaxW + 1):

            F[i][w] = F[i - 1][w]
            if w >= W[i]:
                F[i][w] = max(F[i][w], F[i - 1][w - W[i]] + P[i])

        for h in F:
            print(h)
        print()

    return F[n - 1][MaxW], F



def get_solution(F, W, P, i, w):
    if i == 0:
        if w >= W[0]:
            return [0]
        return []
    if w >= W[i] and F[i][w] == F[i - 1][w - W[i]] + P[i]:
        return get_solution(F, W, P, i - 1, w - W[i]) + [i]
    return get_solution(F, W, P, i - 1, w)


W = [4, 5, 12, 9, 1, 13]
P = [10, 8, 4, 5, 3, 7]
MaxW = 16


M_W, F = knapsack(W, P, MaxW)
print(M_W)


solution = get_solution(F, W, P, len(F) - 1, MaxW)
print(solution)
