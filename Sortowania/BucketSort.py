from random import randint, seed


def bucket_sort(T):
    a, n, idx, v_max, length = 0, len(T), 0, 0, 0

    for i in range(n):
        if abs(T[i]) > v_max:
            v_max = abs(T[i])

    while v_max > 1:
        v_max /= 10
        length += 1

    A = [[] * n for _ in range(n)]

    for i in range(len(T)):
        A[int((T[i] / (10 ** length)) * n)].append(T[i])


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


if __name__ == '__main__':
    n = 100
    T = [randint(1, 1000) for i in range(n)]
    print(T)
    T = bucket_sort(T)
    print(T)
