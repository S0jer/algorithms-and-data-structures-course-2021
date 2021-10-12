# Proszę zaimplementować algorytm zliczający liczbę inwersji w tablicy.
# (Inwersja to para indeksów i, j taka, że i < j oraz T[i] > T[j])

import random



def mergesort(T):
    if len(T) <= 1:
        return T
    half = len(T) // 2
    L = mergesort(T[:half])
    R = mergesort(T[half:])
    return merge(L, R)

def merge(L, R):
    i = j = z = 0
    result = []
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


def mergesort_inv(T):
    global licznik
    if len(T) > 1:
        half = len(T) // 2
        L = T[:half]
        R = T[half:]
        mergesort(L)
        mergesort(R)
        i = j = z = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                T[z] = L[i]
                i += 1
            else:
                T[z] = R[j]
                licznik += half - i
                print(licznik)
                j += 1
            z += 1
        while i < len(L):
            T[z] = L[i]
            z += 1
            i += 1
        while j < len(R):
            T[z] = R[j]
            z += 1
            j += 1
    return T


def inversion(T):
    x = 0
    for i in range(len(T)):
        for j in range(i + 1, len(T)):
            if T[i] > T[j]:
                x += 1
    return x

if __name__ == '__main__':
    licznik = 0
    T = [random.randint(1, 100) for i in range(4)]
    print(T)
    x = inversion(T)
    # T = mergesort(T)
    # print(T)
    mergesort_inv(T)
    print(x, licznik)


