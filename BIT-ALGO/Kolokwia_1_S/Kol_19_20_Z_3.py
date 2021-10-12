# [2pkt.] Zadanie 3. Proszę zaproponować algorytm, który dla tablicy liczb całkowitych
# rozstrzyga czy każda liczba z tablicy jest sumą dwóch innych liczb z tablicy. Zaproponowany
# algorytm powinien być możliwie jak najszybszy. Proszę oszacować jego złożoność obliczeniową.

from random import randint


def selection_sort(arr, a, b):
    for i in range(a, b, +1):
        min_i = i
        for j in range(i + 1, b, + 1):
            if arr[j] < arr[min_i]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]


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


def check(A):
    check = 0
    for x in range(len(A)):
        i, j = 0, len(T) - 1
        while i != j:
            if A[i] + A[j] == A[x]:
                check += 1
                break
            elif A[i] + A[j] < A[x]:
                i += 1
            elif A[i] + A[j] > A[x]:
                j -= 1
        if check != x:
            return False
    return True


if __name__ == '__main__':
    n = 10
    # T = [randint(1, 10) for _ in range(n)]
    T = [3, 11, 4, 5, 12, 7, 2, 1, 10, 6, 0, 9, 8]
    print(T)
    quicksort(T, 0, len(T) - 1)
    if check(T) == True:
        print("Tak")
    else:
        print("Nie")
