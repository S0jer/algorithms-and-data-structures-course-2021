# Zadanie 7
# Dostajemy liste wartości, gramy z drugim gracze. Wybieramy zawsze jedną wartość z jednego z końców tablicy i dodajemy
# do swojej sumy, a następnie to samo robi nasz przeciwnik. Zakładając, że przeciwnik gra optymalnie, jaką
# maksymalną sumę możemy uzyskać?


# Pomysł może i dobry ale no ni uja nie działa


def game(A):
    n = len(A)
    dp = [[0] * n for _ in range(n)]
    pref = [i for i in A]

    suma = sum(A)
    print(suma)

    for i in range(n):
        dp[i][i] = A[i]
        if i > 0: pref[i] += pref[i - 1]


    for j in range(1, n):
        for i in range(n - j):
            dp[i][i + j] = pref[i + j] - pref[i]
            dp[i][i + j] -= min(dp[i + 1][i + j], dp[i][i + j - 1])

    for i in dp:
        print(i)

    print(dp[0][n - 1])

A = [2, 2, 4, 2, 5, 4, 5, 1, 1, 2]
B = [1, 4, 5, 6, 7, 3, 1]
game(A)
game(B)
