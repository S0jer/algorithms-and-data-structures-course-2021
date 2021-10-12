
#ma naprawic kopiec poprzez zamiane elementow na zlych pozycjach
def heapify(A, n, i): #n - ilosc wezlow w kopcu, i - potencjalnie zepsuty
    l = 2*i + 1
    r = 2*i + 2
    m = i #m - powininen to byc indeks pod ktorym jest element o najwiekszej wartosci w kopcu
    if l < n and A[l] > A[m]: m = l
    if r < n and A[r] > A[m]: m = r
    if m != i:
        #print(A, A[m], A[i])
        A[m], A[i] = A[i], A[m]
        heapify(A, n, m)

def buildheap(A):
    n = len(A)
    for i in range(((n - 1) -1) // 2, -1, -1):
        heapify(A, n, i)

def heapsort(A):
    n = len(A)
    buildheap(A)
    for i in range(n - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapify(A, i, 0)

def add_to_heap(A, num):
    A.append(num)
    n = len(A) - 1
    parent = (n - 1) // 2
    while parent >= 0:
        if A[n] > A[parent]:
            #print(A[n], A[parent])
            A[n], A[parent] = A[parent], A[n]
            n = parent
            parent = (n - 1) // 2
            #print(A[n], A[parent])
        else:
            break

if __name__ == '__main__':

    A = [9, 5, 4, 8, 6, 3, 1, 2, 7]
    buildheap(A)
    print(A)
    add_to_heap(A, 5)
    print(A)
    heapsort(A)
    print(A)