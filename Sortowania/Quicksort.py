# Proszę zaimplementować algorytm QuickSort do sortowania listy jednokierunkowej.

from random import randint


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[r], A[i + 1] = A[i + 1], A[r]
    return i + 1


def quicksort(T, p, l):
    while p < l:
        q = partition(T, p, l)
        quicksort(T, p, q - 1)
        p = q + 1
    return T


# def partition(A, p, r):
#     idx = magic_five(A, p, r)
#     x = A[idx]
#     i = p - 1
#     A[r], A[idx] = A[idx], A[r]
#     for j in range(p, r):
#         if A[j] <= x:
#             i += 1
#             A[i], A[j] = A[j], A[i]
#     A[r], A[i + 1] = A[i + 1], A[r]
#     return i + 1


def selection_sort(arr, a, b):
    for i in range(a, b, +1):
        min_i = i
        for j in range(i + 1, b, + 1):
            if arr[j] < arr[min_i]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]


def magic_five(A, a, b):
    idx, a_0 = a, a
    if b - a > 4:
        for i in range(a, b + 1, +5):
            selection_sort(A, a, a + 5)
            A[idx], A[a + 2] = A[a + 2], A[idx]
            idx += 1
        if b - a != 0:
            selection_sort(A, a, b + 1)
            A[idx], A[(b + a) // 2] = A[(b + a) // 2], A[idx]
        return magic_five(A, a_0, idx)
    else:
        selection_sort(A, a, b + 1)
        idx = (a + b) // 2
        return idx


T = [randint(1, 1000000) for i in range(400000)]
print(T)
T = quicksort(T, 0, len(T) - 1)
print(T)
