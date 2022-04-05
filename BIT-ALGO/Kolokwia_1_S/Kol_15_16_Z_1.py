# Proszę zaimplementować funkcję void SumSort(int A[], int B[], int n). Funkcja ta przyjmuje na wejściu dwie n
# 2 - elementowe tablice (A i B) i zapisuje w tablicy B taką permutację elementów z A, że:
# Proszę zaimplementować funkcję SumSort tak, by działała możliwie jak najszybciej. Proszę
# oszacować i podać jej złożoność czasową


def partition(A, p, r):
    id = A[r]
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
