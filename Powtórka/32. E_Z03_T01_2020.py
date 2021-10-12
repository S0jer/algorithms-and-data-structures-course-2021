# Pewien eksperyment fizyczny daje w wyniku liczby rzeczywiste postaci ax, gdzie a to pewna stała
# większa od 1 (a > 1) zaś x to liczby rzeczywiste rozłożone równomiernie na przedziale [0, 1].
# Napisz funkcję fast sort, która przyjmuje tablicę liczb z wynikami eksperymentu oraz stałą a i
# zwraca tablicę z wynikami eksperymentu posortowanymi rosnąco. Funkcja powinna działać możliwie jak najszybciej.
# Uzasadnij poprawność zaproponowanego rozwiązania i oszacuj jego złożoność
# obliczeniową. Nagłówek funkcji fast sort powinien mieć postać

from math import inf


def fast_sort(T, a):
    n = len(T)
    T = bucket_sort(T)

    for i in range(n):
        T[i] = a ** T[i]

    return T


def bucket_sort(T):
    n, idx, v_max, v_min = len(T), 0, 0, inf

    for i in range(n):
        if T[i] > v_max:
            v_max = abs(T[i])
        if v_min > T[i]:
            v_min = T[i]

    n = v_max * 10 + 1
    A = [[] * n for _ in range(n)]

    for i in range(len(T)):
        A[int(T[i] * 10)].append(T[i])

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


T = [0.15, 0.1, 0.12, 0.2, 0.5, 0.7, 0.3, 0.4, 0.8, 0.6, 0.9, 1]
a = 2

print(fast_sort(T, a))
