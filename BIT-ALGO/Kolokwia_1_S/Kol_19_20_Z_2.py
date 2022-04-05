# [2pkt.] Zadanie 2. Mamy n żołnierzy różnego wzrostu i nieuporządkowaną tablicę, w której
# podano wzrosty żołnierzy. Żołnierze zostaną ustawieni na placu w szeregu malejąco względem
# wzrostu. Proszę zaimplementować funkcję:
# section(T,p,q)
# która zwróci tablicę ze wzrostami żołnierzy na pozycjach od p do q włącznie. Użyty algorytm
# powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić 1-2 zdaniowy opis
# algorytmu oraz proszę oszacować jego złożoność czasową.


from random import randint, shuffle, seed


def quicksort(T, p, l):
    while p < l:
        q = partition(T, p, l)
        quicksort(T, p, q - 1)
        p = q + 1
    return T


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[r], A[i + 1] = A[i + 1], A[r]
    return i + 1


def select(A, p, r, k):
    if p == r:
        return p
    q = partition(A, p, r)
    if q == k:
        return q
    elif k < q:
        return select(A, p, q - 1, k)
    else:
        return select(A, q + 1, r, k)


def section(A, p, q):
    a = select(A, 0, len(A) - 1, p)
    b = select(A, 0, len(A) - 1, q)
    print(A)
    print(A[a:b + 1])


if __name__ == '__main__':
    n, p, q = 15, 4, 7
    A = [randint(1, 100) for _ in range(n)]
    print(A)
    section(A, p, q)
    A.sort()
    print(A)
