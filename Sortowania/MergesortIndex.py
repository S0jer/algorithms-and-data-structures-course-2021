def mergeSort(T, l, r):
    if r - l >= 2:
        mid = (l + r) // 2
        mergeSort(T, l, mid)
        mergeSort(T, mid, r)
        merge(T, l, mid, r)
    return T


def merge(T, l, mid, r):
    result = []
    idxL, idxR = l, mid

    while idxL < mid and idxR < r:
        if T[idxL][0] <= T[idxR][0]:
            result.append(T[idxL])
            idxL += 1
        else:
            result.append(T[idxR])
            idxR += 1

    if idxL == mid:
        result += T[idxR:r]
    else:
        result += T[idxL:mid]
    T[l:r] = result

    return T