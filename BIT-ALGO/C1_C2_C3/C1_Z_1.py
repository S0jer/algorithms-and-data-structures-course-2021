# Mamy dane n punktów (x, y) w okręgu o promieniu k (liczba naturalna), tzn 0 <= x^2 + y^2 <= k, które są w nim
# równomiernie rozłożone, tzn. prawdopodobieństwo znalezienia punktu na danym obszarze jest proporcjonalne do pola
# tego obszaru. Napisz algorytm, który w czasie O(n) psosrtuje punkty po ich odległości od punktu (0, 0), tzn.
# d = sqrt(x^2 + y^2)

from random import randint
from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def printpoints(A):
    for i in A:
        print("(", i.x, ",", i.y, ")", end=' | ')
    print("\n")


def distance(a):
    d = sqrt((a.x) ** 2 + (a.y) ** 2)
    return d


def partition(A, p, r):
    x = A[r][1]
    i = p - 1
    for j in range(p, r):
        if A[j][1] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[r], A[i + 1] = A[i + 1], A[r]
    return i + 1


def quicksort(T, p, l):
    while p < l:
        q = partition(T, p, l)
        quicksort(T, p, q - 1)
        p = q + 1


def distance_sort(A, k):
    Bucket = [[] for _ in range(k)]
    for a in A:
        d = int(distance(a)) + 1
        w = k // d
        Bucket[w].append((a, d))
    for i in Bucket:
        quicksort(i, 0, len(i) - 1)
    idx = 0
    for i in range(k - 1, -1, -1):
        j = 0
        if len(Bucket[i]) != 0:
            while j < len(Bucket[i]):
                A[idx] = Bucket[i][j][0]
                idx += 1
                j += 1
    return A


if __name__ == '__main__':
    n = 10
    k = int(sqrt(n ** 2 + n ** 2)) + 1
    A = [Point(randint(1, n), randint(1, n)) for _ in range(10)]
    printpoints(A)
    A = distance_sort(A, k)
    printpoints(A)
