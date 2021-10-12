from zad3testy import runtests


def SortTab(T, P):
    n = len(P)
    m = len(T)
    sections = [[] for _ in range(n)]

    for i in range(m):
        for j in range(n):
            if P[j][0] <= T[i] <= P[j][1]:
                sections[j].append(T[i])
                break

    idx = 0
    for j in range(n):
        bucket_sort(sections[j])
        for z in range(len(sections[j])):
            T[idx] = sections[j][z]
            idx += 1


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


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_i = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_i]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]
    return arr


runtests(SortTab)
