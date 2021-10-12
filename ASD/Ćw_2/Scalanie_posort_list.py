# Proszę zaproponować/zaimplementować algorytm scalający k posortowanych tablic o
# łącznej długości n w jedną posortowaną tablicę w czasie O(n ∗ log(k)).

import random, time


def merge(L, R):
    i, j, z, result = 0, 0, 0, []
    result += L[:]
    result += R[:]
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            result[z] = L[i]
            i += 1
        else:
            result[z] = R[j]
            j += 1
        z += 1
    for a in range(j, len(R)):
        result[z] = R[a]
        z += 1
    for a in range(i, len(L)):
        result[z] = L[a]
        z += 1
    return result


def mergesort(T):
    if len(T) <= 1:
        return T
    half = len(T) // 2
    L = mergesort(T[:half])
    R = mergesort(T[half:])
    return merge(L, R)


def scal(T):
    T_R = []
    for i in range(len(T)):
        T_R += T[i]
    T_R = mergesort(T_R)
    return T_R


# T = [[random.randint(0,100) for i in range(10)] for j in range(8)]
T = [[7, 13, 13, 99],
     [1, 19, 27, 34],
     [2, 25, 32, 60],
     [0, 3, 7, 11],
     [1, 3, 5, 15]]

T_s = scal(T)
print(T_s)
