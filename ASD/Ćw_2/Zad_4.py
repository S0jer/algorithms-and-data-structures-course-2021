# Zadanie 4. (Pojemniki z wodą) Mamy serię pojemników z wodą, połączonych (każdy z każdym) rurami.
# Pojemniki maja kształty prostokątów, rury nie maja objetosci (powierzchni). Każdy pojemnik opisany jest
# przez współrzędne lewego górnego rogu i prawego dolnego rogu.
# Wiemy, ze do pojemników nalano A “powierzchni” wody (oczywiście woda rurami spłynęła do najniźszych
# pojemników). Proszę zaproponować algorytm Obliczający ile pojemników zostało w pełni zalanych.


from random import randint


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def capacity(A):
    v = abs(A[0].x - A[1].x) * abs(A[0].y - A[1].y)
    return v


def partition(A, p, r):
    x = min(A[r][0].y, A[r][1].y)
    i = p - 1
    for j in range(p, r):
        if min(A[j][0].y, A[j][1].y) <= x:
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


def water(A, w_v):
    V, suma = [], 0
    quicksort(A, 0, len(A) - 1)
    for a in A:
        v = capacity(a)
        V.append(v)
        suma += v
    if suma < w_v:
        return len(A)
    buckets, i = 0, 0
    while w_v > 0 or i < len(A):
        z = i + 1
        suma_c = V[i]
        while z < len(A) and A[i][0].y > A[z][1].y:
            suma_c += abs(A[z][0].x - A[z][1].x) * abs(A[i][0].y - A[z][1].y)
            V[z] -= abs(A[z][0].x - A[z][1].x) * abs(A[i][0].y - A[z][1].y)
            z += 1
        w_v -= suma_c
        if w_v >= 0:
            buckets += 1
        i += 1
    return buckets


if __name__ == '__main__':
    A = [(Point(-1, 7), Point(1, 0)), (Point(2, 2), Point(6, -2)), (Point(7, 4), Point(12, 1))]
    w_v = 44
    print(water(A, w_v))
