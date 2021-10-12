from random import randint


def binarySearch(T, i, j, x):
    if (i > j):
        return None
    c = (i + j) // 2
    if (T[c] == x):
        retval = binarySearch(T, i, c - 1, x)
        if (retval == None): return c
        return retval
    if (T[c] > x):
        return binarySearch(T, i, c - 1, x)
    else:
        return binarySearch(T, c + 1, j, x)


def binaryCount(T, i, j, x):
    sum = 0
    c = (i + j) // 2
    if (i < j):
        sum += binaryCount(T, i, c, x)
        sum += binaryCount(T, c + 1, j, x)
        # print(sum)
    else:
        if T[c] == x:
            return 1
        else:
            return 0

    return sum


def countsort(A, k):
    C = [0]
    k
    B = [0]
    len(A)

    for i in range(len(A)):
        C[A[i]] += 1

    for i in range(1, k):
        C[i] = C[i] + C[i - 1]

    for i in range(len(A) - 1, -1, -1):
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]

    for i in range(len(A)):
        A[i] = B[i]


def zaddom(A):
    x = 0
    while 2 ** x < len(A):
        x += 1
    C = []
    for i in range(len(A)):
        if binarySearch(C, 0, len(C) - 1, A[
            i]) == None:  # dla kazdego z n elementów w tablicy dlugosci log(n) szukam bs'em czy element nalezy
            j = len(C) - 1
            C.append(A[i])
            while C[j] > C[j + 1] and j >= 0:
                C[j], C[j + 1] = C[j + 1], C[j]
                j -= 1
            if len(C) >= x:
                break
    D = [0] * x
    for i in A:
        D[binarySearch(C, 0, len(C) - 1, i)] += 1
    iter = 0
    for i in range(len(C)):
        id = D[i]
        while id > 0:
            A[iter] = C[i]
            id -= 1
            iter += 1


if __name__ == '__main__':
    T = [randint(1, 5) for i in range(10)]
    # T = sort(T)
    print(T)
    zaddom(T)
    print(T)
