# Dana jest tablica liczb rzeczywistych wielkości n reprezentująca kopiec minimum.
# Mając daną liczbę rzeczywistą x sprawdź, czy k-ty najmnijeszy element jest większy lub równy x.


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


def search(A, k, x):
    counter = 1
    while counter != k:
        A.pop(0)
        heapify_min(A, len(A), 0)
        counter += 1
    print(A)
    if A[0] >= x:
        return True
    else:
        return False


if __name__ == '__main__':
    A = [10, 9, 8, 4, 3, 2, 1, 6, 7, 5]
    buildheap_min(A)
    print(A)
    print(search(A, 6, 2))
