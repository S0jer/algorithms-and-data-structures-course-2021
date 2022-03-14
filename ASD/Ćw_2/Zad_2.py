# Proszę zaimplementować algorytm zliczający liczbę inwersji w tablicy.
# (Inwersja to para indeksów i, j taka, że i < j oraz T[i] > T[j])

import random


def mergesort_inv(T):
    global licznik
    if len(T) > 1:
        half = len(T) // 2
        L = T[:half]
        R = T[half:]
        mergesort_inv(L)
        mergesort_inv(R)
        i = j = z = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
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
    T = [random.randint(1, 100) for i in range(40)]
    print(T)
    x = inversion(T)
    mergesort_inv(T)
    print(x, licznik)
