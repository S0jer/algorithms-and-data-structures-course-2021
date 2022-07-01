def partition(arr, lo, hi):
    i = lo
    j = lo
    k = hi
    mid = arr[lo]

    while j <= k:
        if arr[j] < mid:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
        elif arr[j] > mid:
            arr[j], arr[k] = arr[k], arr[j]
            k -= 1
        else:
            j += 1

    return i - 1, j


def _quicksort(arr, lo, hi):
    if lo < hi:
        i, j = partition(arr, lo, hi)
        _quicksort(arr, lo, i)
        _quicksort(arr, j, hi)


def quicksort(arr):
    return _quicksort(arr, 0, len(arr) - 1)
