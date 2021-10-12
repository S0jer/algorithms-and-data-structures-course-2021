# Pociagi

def platform(A, m):
    n = len(A)
    trains = []
    cnt = 1

    insert_heap(trains, A[0][1])
    for i in range(1, n):

        if A[i][0] >= trains[0]:
            delete_heap(trains, trains[0])
            cnt -= 1

        insert_heap(trains, A[i][1])
        cnt += 1

        print(trains)
        if cnt > m:
            return False

    return True


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


def insert_heap(A, num):
    A.append(num)
    n = len(A) - 1
    parent = (n - 1) // 2
    while parent >= 0:
        if A[n] < A[parent]:
            A[n], A[parent] = A[parent], A[n]
            n = parent
            parent = (n - 1) // 2
        else:
            break


def delete_heap(A, num):
    A.remove(num)
    heapify_min(A, len(A), 0)


A = [(7, 9), (7, 7.34), (7.40, 8), (10, 10.21), (10.12, 10.17), (10.34, 11), (10.54, 10.57), (12, 12.3), (12, 13.32),
     (12.30, 12.43), (12.42, 13.32), (14, 14.21)]

print(platform(A, 3))
