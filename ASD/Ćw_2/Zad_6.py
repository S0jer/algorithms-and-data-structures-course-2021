# Zadanie 6 (największy przedział). Dany jest ciąg przedziałów domkniętych [a1, b1], . . . ,[an, bn]. Proszę
# zapropnować algorytm, który znajduje taki przedział [at, bt], w którym w całości zawiera się jak najwięcej
# innych przedziałów.

def quicksort(A, p, r):
    while p < r:
        q = partition(A, p, r)
        if (q - p) < (r - p):
            quicksort(A, p, q - 1)
            p = q + 1
        else:
            quicksort(A, q + 1, r)
            r = q - 1


def partition(A, p, r):
    x = A[r][0][1]
    i = p - 1
    for j in range(p, r):
        if A[j][0][1] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def przedzialy(T):
    n, mx, ma, mb, A = len(T), 0, 0, 0, []

    for i in range(n):
        A.append([T[i], 0])
    quicksort(A, 0, len(A) - 1)
    print(A)

    for i in range(n):
        for j in range(i, -1, -1):
            if A[i][0][0] > A[j][0][1]:
                break
            if A[i][0][0] < A[j][0][0]:
                A[i][1] += 1
                if A[i][1] > mx:
                    # ma = A[i][0][0]
                    # mb = A[i][0][1]
                    mx = A[i][1]
    print(A)
    return mx


if __name__ == '__main__':
    ilel_max, ilep_max, i_max, j_max = 0, 0, 0, 0
    # A = [(-1, 10), (-2, 13), (4, 11), (2, 11)]
    A = [(1, 6), (3, 5), (2, 10), (4, 7), (5, 8), (9, 11)]
    print(przedzialy(A))
