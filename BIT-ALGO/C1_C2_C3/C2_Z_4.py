# Mamy tablicę z intami (x, y). Punkt A dominuje punkt B gdy x_A > x_B i y_A > y_B
# Napisz funkcję która poda liczność najmniejszego zbioru z nich by wybrane punkty dominowały wszystkie.

from random import randint


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def printpoints(A):
    for i in A:
        print("(", i.x, ",", i.y, ")", end=' | ')
    print("\n")


def insertion_sort_x(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i].x
        j = i - 1
        while j >= 0 and arr[j].x > key:
            arr[j + 1], arr[j] = arr[j], arr[j + 1]
            j -= 1
    return arr


def insertion_sort_y(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i].y
        j = i - 1
        while j >= 0 and arr[j].y > key:
            arr[j + 1], arr[j] = arr[j], arr[j + 1]
            j -= 1
    return arr


def dominant(A):
    X, Y, D = [], [], []
    for i in A:
        X.append(i)
        Y.append(i)
    X = insertion_sort_x(X)
    Y = insertion_sort_y(Y)

    while len(X) > 0:
        check = X[len(X) - 1]
        if check not in D:
            D.append(check)
        while Y[0] is not check:
            Y.pop(0)
        Y.pop(0)
        X = []
        for j in Y:
            X.append(j)
        X = insertion_sort_x(X)
    return D


def dominant_S(A):
    X = insertion_sort_x(A[:])
    Y = insertion_sort_y(A[:])
    D = []
    while len(X) > 0:
        check = X[len(X) - 1]
        if check not in D:
            D.append(check)
        while Y[0] is not check:
            Y.pop(0)
        Y.pop(0)
        X = insertion_sort_x(Y[:])
    return D


if __name__ == '__main__':
    A = [Point(randint(1, 100), randint(1, 100)) for _ in range(50)]
    printpoints(A)
    D = dominant(A)
    E = dominant_S(A)
    printpoints(D)
    printpoints(E)
