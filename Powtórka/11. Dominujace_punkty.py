# Mamy tablicę z intami (x, y). Punkt A dominuje punkt B gdy x_A > x_B i y_A > y_B
# Napisz funkcję która poda liczność najmniejszego zbioru z nich by wybrane punkty dominowały wszystkie.

from random import randint
from math import inf


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def printpoints(A):
    for i in A:
        print("(", i.x, ",", i.y, ")", end=' | ')
    print("\n")


def printpoints_P(A):
    for i in range(len(A)):
        print("(", A[i][1].x, ",", A[i][1].y, ")", end=' | ')
    print("\n")


def insertion_sort_x(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i][1].x
        j = i - 1
        while j >= 0 and arr[j][1].x > key:
            arr[j + 1], arr[j] = arr[j], arr[j + 1]
            j -= 1


def insertion_sort_y(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i][1].y
        j = i - 1
        while j >= 0 and arr[j][1].y > key:
            arr[j + 1], arr[j] = arr[j], arr[j + 1]
            j -= 1


def dominant(A):
    n = len(A)
    X, Y, D = [], [], []
    check = [0 for _ in range(n)]
    j, i = n - 1, 0

    for a in range(n):
        X.append([a, A[a]])
        Y.append([a, A[a]])

    insertion_sort_x(X)
    insertion_sort_y(Y)

    while j > 0:
        if check[X[j][0]] == 0:
            D.append(A[X[j][0]])
            while Y[i][1] != X[j][1] and i < n:
                check[Y[i][0]] = 1
                i += 1

        j -= 1

    return D


if __name__ == '__main__':
    A = [Point(randint(1, 15), randint(1, 15)) for _ in range(10)]
    printpoints(A)
    D = dominant(A)
    printpoints(D)
