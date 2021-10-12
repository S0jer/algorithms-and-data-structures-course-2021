from random import randint, seed


def merge(L, R):
    i, j, z, result = 0, 0, 0, []
    result += L[:]
    result += R[:]
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
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


def mergesort(T):
    if len(T) <= 1:
        return T
    half = len(T) // 2
    L = mergesort(T[:half])
    R = mergesort(T[half:])
    return merge(L, R)


seed(42)

n = 10
T = [randint(1, 10) for i in range(10)]

print("przed sortowaniem: T =", T)
T = mergesort(T)
print("po sortowaniu    : T =", T)

for i in range(len(T) - 1):
    if T[i] > T[i + 1]:
        print("Błąd sortowania!")
        exit()

print("OK")
