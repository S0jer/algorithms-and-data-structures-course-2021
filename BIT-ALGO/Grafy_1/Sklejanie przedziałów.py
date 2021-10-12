#


def glue(A, p):
    n = len(A)
    A.sort(key=lambda A: A[0])
    cnt = 0
    print(A)

    for i in range(n - 1):
        A[i] = (A[i], cnt)
        cnt += 1
    A[n - 1] = (A[n - 1], cnt)
    cnt += 1
    print(A)
    G = [[0] * (cnt) for _ in range(cnt)]

    for i in range(n):
        for j in range(i, n):
            if A[i][0][1] == A[j][0][0]:
                G[A[i][1]][A[j][1]] = 1

    return DFS(A, G, p)


def DFS(A, G, p):
    n = len(G)

    for i in range(n):
        c = [0]
        if p[0] == A[i][0][0]:
            c = DFSVisit(A, G, i, p, c)
            print(c)
            if sum(c) > 0:
                return True
    return False


def DFSVisit(A, G, u, p, c):
    if A[u][0][1] == p[1]:
        c.append(1)

    n = len(G)
    for i in range(n):
        if G[u][i] == 1:
            DFSVisit(A, G, i, p, c)

    return c


if __name__ == '__main__':
    A = [(1, 2), (2, 5), (5, 7), (5, 6), (2, 3), (3, 7), (7, 9), (9, 11), (2, 9), (9, 10), (10, 69)]
    print(glue(A, (1, 69)))
