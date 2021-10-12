from random import randint
from math import log


def fast_sort(tab, a):
    tab = bucket_sort(tab, a)

    return tab


def bucket_sort(T, a):
    n, idx, v_max, length = len(T), 0, 0, 0

    for i in range(n):
        if abs(T[i]) > v_max:
            v_max = abs(T[i])

    while v_max > 1:
        v_max /= 10
        length += 1
    print(length)
    A = [[] * n for _ in range(n)]

    for i in range(n):
        A[int((log(a, T[i]) / (10 ** length)) * n)].append(T[i])
    print(A)
    for j in range(len(A)):
        if len(A[j]) > 1:
            A[j] = selection_sort(A[j])
        for i in A[j]:
            T[idx] = i
            idx += 1

    return T


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_i = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_i]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]
    return arr


n = 8
T = [0.1, 0.2, 0.5, 0.7, 0.3, 0.4, 0.8, 0.6, 0.9]

print(T)
print(fast_sort(T, 2))

flaga = False
for i in range(n - 1):
    if T[i] > T[i + 1]:
        print("Błąd!")
        flaga = True
        break

if flaga == False:
    print("OK!")
