def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[r], A[i + 1] = A[i + 1], A[r]
    return i + 1


def select(A, p, r, k):
    if p == r:
        return
    q = partition(A, p, r)
    if q == k:
        return
    elif k < q:
        return select(A, p, q - 1, k)
    else:
        return select(A, q + 1, r, k)


A = [11, 5, 2, 64, 8, 100, 58, 15, 12, 15, 25]
T = [3, 11, 4, 5, 12, 7, 2, 1, 10, 6, 0, 9, 8]
B = [11, 5, 2, 64, 8, 100, 58, 15, 12, 15, 25, 34, 12, 4, 34, 5, 23, 4, 54, 23, 12, 14, 35, 76]

print(B)
select(B, 0, len(B) - 1, 2)
select(B, 2, len(B) - 1, 8)
print(B)
