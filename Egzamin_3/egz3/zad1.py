# Paweł Jaśkowiec

# pomysł polega na znalezieniu rosnacych i malejacych podciagów od od punktu i=tego oraz znalezienu w tym zestawieniu
# najdluzszego rosnacego/malejacego badz malejaco-rosnacego
import operator

from zad1testy import runtests


def mr(X):
    n = len(X)

    i = 0
    dp = [[[[], 0], [[], 0]] for _ in range(n)]

    while i < n - 1:
        M, R = [X[i]], [X[i]]
        last_m, last_r = i, i
        j = i + 1
        check = [0, 0]
        while j < n and (check[0] == 0 or check[1] == 0):
            if X[last_m] > X[j] and check[0] == 0:
                last_m = j
                M.append(X[j])
            else:
                check[0] = 1
            if X[last_r] < X[j] and check[1] == 0:
                last_r = j
                R.append(X[j])
            else:
                check[1] = 1

            j += 1

        if len(dp[i][0][0]) < len(M):
            dp[i][0][0] = M
            dp[i][0][1] = last_m

        if len(dp[i][1][0]) < len(R):
            dp[i][1][0] = R
            dp[i][1][1] = last_r

        i += 1

    result = []
    L_M, L_R, L_MR = [], [], []

    for i in range(n):
        if len(dp[i][0][0]) > len(L_M):
            L_M = dp[i][0][0]
            for j in range(i + len(L_M), n):
                if len(dp[i][0][0] + dp[j][1][0]) > len(L_MR):
                    L_MR = dp[i][0][0] + dp[j][1][0]

        if len(dp[i][1][0]) > len(L_R):
            L_R = dp[i][0][0]

    if len(L_R) > len(result):
        result = L_R

    if len(L_M) > len(result):
        result = L_M

    if len(L_MR) > len(result):
        result = L_MR

    return result

def mr(X):
    lis_1 = lis(X)
    lis_2 = lis2(X)
    index_max = max(range(len(X)), key=X.__getitem__)
    printsolution(X, lis_1[2], index_max)
    print(lis_1)
    print(lis_2)


    pass

def lis(A):
    n = len(A)
    F = [-1]*n
    P = [-1]*n
    for i in range(1, n):
        for j in range(i):
            if A[j] < A[i] and F[j] + 1 > F[i]:
                F[i] = F[j] + 1
                P[i] = j

    return (max(F), F, P)

def lis2(A):
    n = len(A)
    F = [-1]*n
    P = [-1]*n
    for i in range(1, n):
        for j in range(i):
            if A[j] > A[i] and F[j] + 1 > F[i]:
                F[i] = F[j] + 1
                P[i] = j

    return (max(F), F, P)


def printsolution(A,P,i):
    if P[i] != -1:
        printsolution(A, P, P[i])
    print(A[i])

runtests(mr)
