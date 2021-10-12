# Paweł Jaśkowiec, 406165

# Pomysł polega na braniu przedziałów o długości 2*k i sortowaniu ich, gdzie k elementów znajdzie się na swoim miejscu
# następnie przesunięcie listy o k elementów do przodu, ponieważ one znalazły się już na swoim miejscu.

# Dla k == 1 nie działało i nie udało mi się naprawić, w testach gryzie się coś z sortowaniem którego użyłem :/

# Złożoność: (n/k)*(2*k*log(2*k))

from zad2testy import runtests


class Node:
    def __init__(self):
        self.val = None
        self.next = None


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



def printlist(L):
    while L != None:
        print(L.val, "->", end=" ")
        L = L.next
    print("|")


def SortH(p, k):
    start = p
    end = p
    while start.next is not None:

        cnt = 0
        while cnt < 2*k + 1 and end.next is not None:
            end = end.next
            cnt += 1

        if end.next is None:
            quicksort(start, None)
        else:
            quicksort(start, end)

        cnt = 0
        while cnt <= k and start.next is not None:
            start = start.next
            cnt += 1

    return p




L0 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]
L1 = [2, 5, 3, 7, 13, 11, 17, 19, 29, 23, 31, 37, 43, 41, 47, 53, 59, 67, 61, 73, 71, 79, 83, 89]
L2 = [2, 3, 5, 7, 11, 13, 17, 19, 31, 23, 29, 43, 41, 37, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]
L5 = [2, 11, 5, 7, 3, 31, 13, 19, 37, 29, 17, 23, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]
L10 = [2, 3, 11, 7, 5, 23, 17, 19, 13, 29, 41, 37, 31, 89, 47, 53, 59, 61, 67, 71, 73, 43, 83, 79]
L20 = [2, 79, 5, 7, 11, 23, 17, 19, 13, 29, 3, 37, 41, 89, 47, 53, 59, 61, 31, 71, 73, 67, 83, 43]


runtests(SortH)
