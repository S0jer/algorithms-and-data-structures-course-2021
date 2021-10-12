# 1. Napisać funkcję: void sortString(string A[]); Funkcja sortuje tablicę n stringów różnej
# długości. Można założyć, że stringi składają się wyłącznie z małych liter alfabetu łacińskiego.


def radix(A, j):
    for i in range(len(A)):
        while i > 0:
            if (A[i][j] < A[i - 1][j]):
                A[i], A[i - 1] = A[i - 1], A[i]
            i -= 1
    return A


def sortString(T):
    A = []
    for i in T:
        while len(i) >= len(A):
            A.append([])
        A[len(i)].append(i)
    for i in range(len(A) - 1, 0, -1):
        if len(A[i]) > 1:
            j = i - 1
            if j < 0:
                j = 0
            A[i] = radix(A[i], j)
        if A[i] != [] and i != 0:
            A[i - 1] = A[i] + A[i - 1]
    A = A[0]
    return A


if __name__ == '__main__':
    A = ["kra", "afart", "kfot", "kadeit", "ati", "kil"]
    print(A)
    A = sortString(A)
    print(A)
