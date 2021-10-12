from random import randint, seed


def f_max(T):
    i_max, d = 0, 0
    for i in T:
        if i > i_max:
            i_max = i
    while i_max != 0:
        i_max //= 10
        d += 1
    return d


def radix_sort(T, D):
    d = f_max(T) - D
    A = [[] for _ in range(10)]
    for j in range(len(T)):
        a = T[j]
        a = (a // (10 ** d)) % 10
        A[a].append(T[j])
    j = 0
    for z in A:
        for x in z:
            T[j] = x
            j += 1
    if D != 0:
        return radix_sort(T, D - 1)
    else:
        return T

# Tablica i według której litery
def radix(A, j):
    for i in range(len(A)):
        while i > 0:
            if (A[i][j] < A[i - 1][j]):
                A[i], A[i - 1] = A[i - 1], A[i]
            i -= 1
    return A


if __name__ == '__main__':
    seed(42)
    T = [randint(1, 10) for i in range(10)]
    T_S = ["kraatr","artat","kot","kit","ati","kil"]
    print(T)
    T = radix_sort(T, f_max(T))
    print(T, "\n")
    A = ["kra", "art", "kot", "kit", "ati", "kil"]
    print(radix(A, 2))
    print(radix(A, 1))
    print(radix(A, 0))