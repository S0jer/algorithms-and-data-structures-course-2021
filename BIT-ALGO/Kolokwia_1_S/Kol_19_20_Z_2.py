# [2pkt.] Zadanie 2. Mamy n żołnierzy różnego wzrostu i nieuporządkowaną tablicę, w której
# podano wzrosty żołnierzy. Żołnierze zostaną ustawieni na placu w szeregu malejąco względem
# wzrostu. Proszę zaimplementować funkcję:
# section(T,p,q)
# która zwróci tablicę ze wzrostami żołnierzy na pozycjach od p do q włącznie. Użyty algorytm
# powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić 1-2 zdaniowy opis
# algorytmu oraz proszę oszacować jego złożoność czasową.


from random import randint, shuffle, seed


def selection_sort(arr, a, b):
    for i in range(a, b, +1):
        min_i = i
        for j in range(i + 1, b, + 1):
            if arr[j] < arr[min_i]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]


def magic_five(A, a, b):
    id, a_0 = a, a
    if b - a > 4:
        for i in range(a, b + 1, +5):
            selection_sort(A, a, a + 5)
            A[id], A[a + 2] = A[a + 2], A[id]
            id += 1
        if b - a != 0:
            selection_sort(A, a, b + 1)
            A[id], A[(b + a) // 2] = A[(b + a) // 2], A[id]
        return magic_five(A, a_0, id)
    else:
        selection_sort(A, a, b + 1)
        id = (a + b) // 2
        return id


def quicksort(T, p, l):
    while p < l:
        q = partition(T, p, l)
        quicksort(T, p, q - 1)
        p = q + 1
    return T


def partition(A, p, r):
    id = magic_five(A, p, r)
    x = A[id]
    i = p - 1
    A[r], A[id] = A[id], A[r]
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
    quicksort(A, a, b)
    print(A[a:b + 1])


if __name__ == '__main__':
    n, p, q = 15, 4, 7
    A = [randint(1, 100) for _ in range(n)]
    print(A)
    section(A, p, q)
