# Dane są trzy zbiory reprezentowane przez tablice: A, B i C. Napisz algorytm, który powie,
# czy istnieje tak trójka a,b,c z odpowiednio A, B, C, że a + b = c

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


def quicksort(T, p, l):
    while p < l:
        q = partition(T, p, l)
        quicksort(T, p, q - 1)
        p = q + 1
    return T


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


def three_sets(A, B, C):
    A = quicksort(A, 0, len(A) - 1)
    B = quicksort(B, 0, len(A) - 1)
    for c in range(len(C)):
        i, j = 0, len(B) - 1
        if A[len(A) - 1] + B[j] > C[c] and A[i] + B[0] < C[c]:
            while i <= len(A) - 1 or j >= 0:
                if A[i] + B[j] == C[c]:
                    return True
                if A[i] + B[j] < C[c] and i < len(A) - 1:
                    i += 1
                if A[i] + B[j] > C[c] and j > 0:
                    j -= 1
    return False


if __name__ == '__main__':
    A = [randint(1, 100) for _ in range(40)]
    B = [randint(1, 100) for _ in range(40)]
    C = [randint(90, 100) for _ in range(3)]
    print(three_sets(A, B, C))
