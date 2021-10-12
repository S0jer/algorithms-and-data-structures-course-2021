# Paweł Jaśkowiec, 406165


# Sortuję po początkach i wrzucam do kolejki po końcach przedziału elementy tablicy A
# gdy kolejka się zapełni biorę k elementów i sprawdzam czy dane k przedziałów daje najlepszy wynik


from zad3testy import runtests


def kintersect(A, k):
    n = len(A)

    for i in range(n):
        A[i] = [A[i], i]

    A = mergesort(A)

    result, result_L = [-1] * k, 0
    if k == 1:
        for a in range(n):
            if A[a][0][1] - A[a][0][0] >= result_L:
                result_L = A[a][0][1] - A[a][0][0]
                result = [A[a][1]]

        return result

    for i in range(n):

        C, cnt = [-1] * k, 0
        C[cnt] = A[i]
        for j in range(n - 1, -1, -1):
            if i != j and A[j][0][0] <= A[i][0][0] and A[j][0][1] > A[i][0][0]:
                if cnt < k - 1:
                    cnt += 1
                    C[cnt] = A[j]

                elif cnt == k - 1:
                    id_min = 1
                    for x in range(1, k):
                        if C[x][0][1] < C[id_min][0][1]:
                            id_min = x

                    if A[j][0][1] > C[id_min][0][1]:
                        C[id_min] = A[j]

        if cnt == k - 1:
            id_max = 0
            for y in range(k):
                if C[id_max][0][1] >= C[y][0][1]:
                    id_max = y

            l_c = abs(C[id_max][0][1] - C[0][0][0])
            if l_c > result_L:
                result_L = l_c
                result = []
                for z in range(k):
                    result.append(C[z][1])

    return result


def merge(L, R):
    i, j, z, result = 0, 0, 0, []
    result += L[:]
    result += R[:]
    while i < len(L) and j < len(R):
        if L[i][0][0] <= R[j][0][0]:
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


runtests(kintersect)
