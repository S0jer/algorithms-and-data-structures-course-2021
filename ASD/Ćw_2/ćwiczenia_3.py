  from random import randint


def partition(T, l, r):
    a = randint(l, r)
    x = T[a]
    T[r], T[a] = T[a], T[r]
    i = l - 1
    for j in range(l, r):
        if T[j] <= x:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[r], T[i + 1] = T[i + 1], T[r]
    return i + 1


def quicksort(T, l, r):
    while l < r:
        q = partition(T, l, r)
        if q - l <= r - q:
            quicksort(T, l, q - 1)
            l = q + 1
        else:
            quicksort(T, q + 1, r)
            r = q - 1
    return T


# T =[10, 33, 22, 22, 1, 23, 12, 9, 22]
# print(quicksort(T,0,len(T)-1))

def dodawanie(heap, v):
    heap.append(v)
    n = len(heap)
    i = n - 1
    j = (i - 1) // 2
    while i > 0 and heap[j] <= v:
        heap[i], heap[j] = heap[j], heap[i]
        i = j
        j = (i - 1) // 2
    return heap


# heap = [6]
# head = dodawanie(heap, 4)
# head = dodawanie(heap, 10)
# head = dodawanie(heap, 15)
# head = dodawanie(heap, 2)
# head = dodawanie(heap, 1)
# print(heap)


def quick(T):
    tab = [(0, len(T) - 1)]
    while len(tab):
        left, right = tab.pop()
        if left < right:
            q = partitionH(T, left, right)
            tab.append((q + 1, right))
            tab.append((left, q - 1))


def partitionH(T, left, right):
    pivot = T[left]
    i = left + 1
    j = right
    while True:
        while T[i] < pivot:
            if i == right:
                break
            i += 1

        while T[j] > pivot:
            j -= 1
        print(i, j)
        print(T)
        if i >= j:
            break
        #     return j

        T[i], T[j] = T[j], T[i]
        # i+=1
        # j-=1
    T[left], T[j] = T[j], T[left]
    return j


T = [10, 33, 22, 22, 1, 23, 12, 9, 22]
quick(T)
print(T)

