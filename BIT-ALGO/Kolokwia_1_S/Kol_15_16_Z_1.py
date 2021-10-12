# Proszę zaimplementować funkcję void SumSort(int A[], int B[], int n). Funkcja ta przyjmuje na wejściu dwie n
# 2 - elementowe tablice (A i B) i zapisuje w tablicy B taką permutację elementów z A, że:
# Proszę zaimplementować funkcję SumSort tak, by działała możliwie jak najszybciej. Proszę
# oszacować i podać jej złożoność czasową

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
        return
    q = partition(A, p, r)
    if q == k:
        return
    elif k < q:
        select(A, p, q - 1, k)
    else:
        select(A, q + 1, r, k)


def SumSort(A, B, n):
    for i in range(n, n * n, n):
        select(A, i - n, n * n - 1, i)
    for j in range(len(A)):
        B[j] = A[j]

    return B


A = [1, 1, 6, 2, 1, 3, 4, 4, 0]
B = [0]*len(A)
print(A)
SumSort(A, B, 3)
print(B)
