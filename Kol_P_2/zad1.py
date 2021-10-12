from zad1testy import runtests


def rect(D):
    n = len(D)
    S = [0 for _ in range(n)]
    E = [0 for _ in range(n)]
    R = [0 for _ in range(n)]

    S[0] = (D[0], field(D[0], D[0]))
    E[n - 1] = (D[n - 1], field(D[n - 1], D[n - 1]))

    for i in range(1, n):
        S[i] = (common(S[i - 1][0], D[i]), field(S[i - 1][0], D[i]))
        E[n - 1 - i] = (common(E[n - i][0], D[n - 1 - i]), field(E[n - i][0], D[n - 1 - i]))

    R[0] = E[1][1]
    R[n - 1] = S[n - 2][1]

    for j in range(1, n - 1):
        R[j] = field(S[j - 1][0], E[j + 1][0])

    max_w = -1
    result = -1
    for k in range(n):
        if R[k] > max_w:
            result = k
            max_w = R[k]

    return result


def field(A, B):
    if (A[1] <= B[3] and A[0] <= B[2] and A[2] >= B[0] and A[3] >= B[1]) or (
            B[1] <= A[3] and B[0] <= A[2] and B[2] >= A[0] and B[3] >= A[1]):
        X = abs(max(A[0], B[0]) - min(A[2], B[2])) * abs(max(A[1], B[1]) - min(A[3], B[3]))
        return X
    return 0


def common(A, B):
    if (A[1] <= B[3] and A[0] <= B[2] and A[2] >= B[0] and A[3] >= B[1]) or (
            B[1] <= A[3] and B[0] <= A[2] and B[2] >= A[0] and B[3] >= A[1]):
        X = (max(A[0], B[0]), max(A[1], B[1]), min(A[2], B[2]), min(A[3], B[3]))
        return X
    return (0, 0, 0, 0)


runtests(rect)
