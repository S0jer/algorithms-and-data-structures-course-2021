def buildheap_min(A):
    n = len(A)
    for i in range((n - 2) // 2, -1, -1):
        heapify_min(A, n, i)


def heapify_min(A, n, i):
    l = 2 * i + 1
    r = 2 * i + 2
    m = i
    if l < n and A[l] < A[m]:
        m = l
    if r < n and A[r] < A[m]:
        m = r
    if m != i:
        A[i], A[m] = A[m], A[i]
        heapify_min(A, n, m)


def heapsort_min(A):
    n = len(A)
    buildheap_min(A)
    for i in range(n - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapify_min(A, i, 0)


def buildheap(A):
    n = len(A)
    for i in range((n - 2) // 2, -1, -1):
        heapify(A, n, i)


def heapify(A, n, i):
    l = 2 * i + 1
    r = 2 * i + 2
    m = i
    if l < n and A[l] > A[m]:
        m = l
    if r < n and A[r] > A[m]:
        m = r
    if m != i:
        A[i], A[m] = A[m], A[i]
        heapify(A, n, m)


def heapsort(A):
    n = len(A)
    buildheap(A)
    for i in range(n - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapify(A, i, 0)


def insert_heap(A, num):
    A.append(num)
    n = len(A) - 1
    parent = (n - 1) // 2
    while parent >= 0:
        if A[n] > A[parent]:
            A[n], A[parent] = A[parent], A[n]
            n = parent
            parent = (n - 1) // 2
        else:
            break


def delete_heap(A, num):
    A.remove(num)
    heapify(A, len(A), 0)


if __name__ == '__main__':
    A = [9, 5, 4, 8, 6, 3, 1, 2, 7]
    B = [9, 5, 4, 8, 6, 3, 1, 2, 7]
    buildheap(A)
    buildheap_min(B)
    print(A, B)
    insert_heap(A, 10)
    # heapsort(A)
    # heapsort_min(B)
    print(A, B)
    delete_heap(A, 10)
    print(A)
