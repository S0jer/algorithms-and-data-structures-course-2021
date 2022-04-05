# Paweł Jaśkowiec, 406165

# Algorytm bierze wycinek listy długości 2*k oraz sortuje go za pomocą sortowania quicksort
# następnie przesuwa się o k elementów do przodu ponieważ z faktu iż lista jest k-chaotyczna, k elementów
# znajdzie się na swojej pozycji.

# Złożoność: Quicksort - 2k*log(2k) dla n//k odcinków --> (n//k)*2k*log(2k)

# Dla:
# k = 0(1) -> n*2log(2)
# k = O(log(n)) -> (n//log(n))*2*log(n)*log(2*log(n))
# k = O(n) -> n*log(n)

from zad2testy import runtests


class Node:
    def __init__(self):
        self.val = None
        self.next = None


def SortH(p, k):
    start, prev, end = p, Node(), p
    prev.val = None
    prev.next = start
    p = prev

    # Wyznaczam odcinek długości 2*k
    cnt = 0
    while cnt < 2 * k + 1 and end.next is not None:
        end = end.next
        cnt += 1

    while start.next is not None:

        if end.next is not None:
            endNext = end.next
            end.next = None
            start = qsort(start)
        else:
            start = qsort(start)
            prev.next = start
            break

        prev.next = start
        end = start
        while end.next is not None:
            end = end.next
        end.next = endNext

        # Przesuwam listę o k elementów do przodu ponieważ są one już na swoim miejscu,
        cnt = 0
        while cnt < k + 1 and start.next is not None and end.next is not None:
            prev = prev.next
            start = start.next
            end = end.next
            cnt += 1

    return p.next


def partition(L, end):
    pivot = L  # pivot to pierwszy element, nie ma sensu przechodzic calej listy i brac ostatniego
    head = L  # przechowuje wskaznik na 1 element
    while L.next != end:
        if L.next.val < pivot.val:
            tmp = L.next
            L.next = L.next.next
            tmp.next = head
            head = tmp
        else:
            L = L.next
    return (head, pivot)


def quicksort(L, end):
    if L != end:
        L, p = partition(L, end)
        L = quicksort(L, p)
        p.next = quicksort(p.next, end)
    return L


def qsort(L):
    return quicksort(L, None)


L0 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]
L1 = [2, 5, 3, 7, 13, 11, 17, 19, 29, 23, 31, 37, 43, 41, 47, 53, 59, 67, 61, 73, 71, 79, 83, 89]
L2 = [2, 3, 5, 7, 11, 13, 17, 19, 31, 23, 29, 43, 41, 37, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]
L5 = [2, 11, 5, 7, 3, 31, 13, 19, 37, 29, 17, 23, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]
L10 = [2, 3, 11, 7, 5, 23, 17, 19, 13, 29, 41, 37, 31, 89, 47, 53, 59, 61, 67, 71, 73, 43, 83, 79]
L20 = [2, 79, 5, 7, 11, 23, 17, 19, 13, 29, 3, 37, 41, 89, 47, 53, 59, 61, 31, 71, 73, 67, 83, 43]

runtests(SortH)
