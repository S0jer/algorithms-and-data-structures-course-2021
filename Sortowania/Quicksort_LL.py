from random import randint, seed


class Node:
    def __init__(self):
        self.next = None
        self.value = None


def partition(L, end):
    pivot = L  # pivot to pierwszy element, nie ma sensu przechodzic calej listy i brac ostatniego
    head = L  # przechowuje wskaznik na 1 element
    while L.next != end:
        if L.next.key < pivot.key:
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


def tab2list(A):
    H = Node()
    C = H
    for i in range(len(A)):
        X = Node()
        X.value = A[i]
        C.next = X
        C = X
    return H.next


def printlist(L):
    while L != None:
        print(L.value, "->", end=" ")
        L = L.next
    print("|")


seed(42)

n = 10
T = [randint(1, 100) for i in range(50)]
L = tab2list(T)  # [2, 1, 5, 4, 4, 3, 2, 9, 2,])

print("przed sortowaniem: L =", end=" ")
printlist(L)
L = qsort(L)
print("po sortowaniu    : L =", end=" ")
printlist(L)

if L == None:
    print("List jest pusta, a nie powinna!")
    exit(0)

P = L
while P.next != None:
    if P.value > P.next.key:
        print("Błąd sortowania")
        exit(0)
    P = P.next

print("OK")
