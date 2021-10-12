# Find a triplet having the maximum product in an array


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[r], A[i + 1] = A[i + 1], A[r]
    return i + 1


def quicksort(T, p, l):
    while p < l:
        q = partition(T, p, l)
        quicksort(T, p, q - 1)
        p = q + 1


def triplet_product(A):
    quicksort(A, 0, len(A) - 1)
    if A[0] * A[1] > 0:
        a = A[len(A) - 1] * A[len(A) - 2] * A[len(A) - 3]
        b = A[len(A) - 1] * A[0] * A[1]
        c = A[0] * A[1] * A[2]
        x = max(a, b, c)
    else:
        x = A[len(A) - 1] * A[len(A) - 2] * A[len(A) - 3]
    return x


if __name__ == '__main__':
    A = [-4, 1, -8, 9, 6]
    B = [1, 7, 2, -2, 5]
    print(triplet_product(A))
    print(triplet_product(B))
