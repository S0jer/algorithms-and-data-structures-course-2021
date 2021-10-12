# Problem plecakowy ale liczymy ilość sposobów.

def printT(A):
    for i in A:
        print(i)


def kanpsack_how_much(W, V, MaxW, c_min):
    n = len(W)
    c_max = sum(V)
    dp = [[[0] * (c_max + 1) for _ in range(MaxW + 1)] for _ in range(n)]

    for w in range(W[0], MaxW + 1):
        for c in range(c_min, c_max + 1):
            dp[0][w][c] += 1

    for i in range(1, n):
        for w in range(1, MaxW + 1):
            for c in range(c_min, c_max + 1):
                if w - W[i] >= 0 and c - V[i] >= 0:
                    dp[i][w][c] = dp[i - 1][w][c] + dp[i - 1][w - W[i]][c - V[i]]
                else:
                    dp[i][w][c] = dp[i - 1][w][c]


    for i in dp:
        printT(i)
        print()


W = [1, 2, 3]
V = [2, 1, 3]
W_1 = [1, 2]
V_1 = [3, 1]
W_2 = [4,9,3,1,8,8,7,8,2]
V_2 = [2,4,1,1,7,1,6,8,2]

kanpsack_how_much(W, V, 3, 2)
print()
kanpsack_how_much(W_1, V_1, 3, 2)
print()
kanpsack_how_much(W_2, V_2, 25, 10)
