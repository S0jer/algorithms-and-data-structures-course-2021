def lis(A, z):
    n = len(A)
    F = [1] * n
    P = [-1] * n
    for i in range(1, n):
        for j in range(i):
            if A[j] < A[i] and F[j] + 1 >= F[i]:
                F[i] = F[j] + 1
                P[i] = j
    print(F, P)
    return max(F), F, P


def printsolution(A, P, i):
    if P[i] != -1:
        printsolution(A, P, P[i])
    print(A[i], end=" ")


A = [2,1,4,3]
z = 4
i, F, P = lis(A, z)
# index_max = max(range(len(A)), key=A.__getitem__)
# print(F, "\n", P)
# printsolution(A, P, index_max)
