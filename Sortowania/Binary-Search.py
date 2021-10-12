


def binarySearch(T, i, j, x):
    if i > j:
        return None
    half = (i + j) // 2
    if T[half] == x:
        retval = binarySearch(T, i, half - 1, x)
        if retval == None:
            return half
        return retval
    if T[half] > x:
        return binarySearch(T, i, half - 1, x)
    else:
        return binarySearch(T, half + 1, j, x)



