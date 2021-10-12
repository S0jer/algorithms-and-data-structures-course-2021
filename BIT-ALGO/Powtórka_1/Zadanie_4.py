# Sasha Grey i matrioszka


def put_in(A):
    A.sort(key=lambda A: A[0])
    print(A)
    n = len(A)
    F = [1] * n
    P = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if A[j][0] < A[i][0] and A[j][1] < A[i][1] and F[j] + 1 > F[i]:
                F[i] = F[j] + 1
                P[i] = j

    print(max(F))
    index_max = max(range(len(A)), key=A.__getitem__)
    printsolution(A, P, index_max)


def printsolution(A, P, i):
    if P[i] != -1:
        printsolution(A, P, P[i])
    print(A[i])

A = [(1, 2), (4, 5), (2, 6), (3, 1), (5, 5), (8, 2), (1, 1)]

put_in(A)
