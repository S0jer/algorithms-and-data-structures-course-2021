from random import randint, shuffle, seed


# def magic_five(A, a, b, id, a_0):
#     if a + 5 <= b:
#         selection_sort(A, a, a + 5)
#         print(A)
#         A[id], A[a + 2] = A[a + 2], A[id]
#         return magic_five(A, a + 5, b, id + 1, a_0)
#     elif b - a >= 0 and a != a_0:
#         selection_sort(A, a, b + 1)
#         print(A)
#         A[id], A[(b + a) // 2] = A[(b + a) // 2], A[id]
#         return magic_five(A, a_0, id, id, a_0)
#     else:
#         selection_sort(A, a_0, b + 1)
#         return id
#         id = (a_0 + b) // 2

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
        for i in range(a, b + 1, +5):  # przechodzimy przez podany zakres dzieląc go na grupy po 5 elementów
            selection_sort(A, a, a + 5)  # sortujemy dany fragment
            A[id], A[a + 2] = A[a + 2], A[id]  # przenosimy medianę na początek listy
            id += 1
        if b - a != 0:  # jak w pętli for, dla grupy mniej licznej niż 5 elementów
            selection_sort(A, a, b + 1)
            A[id], A[(b + a) // 2] = A[(b + a) // 2], A[id]
        # wywołujemy dla zakresu tablicy gdzie są mediany
        return magic_five(A, a_0, id)
    else:
        # wyznaczamy medianę z median
        selection_sort(A, a, b + 1)
        id = (a + b) // 2
        return id


def partition(A, p, r):
    id = magic_five(A, p, r)  # (A, p, r ,p ,p)
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
        return A[p]
    q = partition(A, p, r)
    if q == k:
        return A[q]
    elif k < q:
        return select(A, p, q - 1, k)
    else:
        return select(A, q + 1, r, k)


def linearselect(A, k):
    return select(A, 0, len(A) - 1, k)


seed(42)
n = 11
for i in range(n):
    A = list(range(n))
    shuffle(A)
    print(A)
    x = linearselect(A, i)
    if x != i:
        print("Blad podczas wyszukiwania liczby", i)
        exit(0)

print("OK")
