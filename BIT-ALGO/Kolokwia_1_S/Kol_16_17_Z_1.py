# 1. Dana jestr struktura opisująca listę jednokierunkową dla liczb rzeczywistych:
# struct Node{ Node* next; double value; }
# Proszę zaimplementować funkcję void Sort( Node* list ), która otrzymuje na wejściu listę
# liczb rzeczywistych (z wartownikiem), wygenerowaną zgodnie z rozkładem jednostajnym na
# przedziale [0,10) i sortuje jej zawartość w kolejności niemalejącej. Funkcja powinna być możliwie
# jak najszybsza (biorąc pod uwagę warunki zadania). Proszę oszacować złożoność
# zaimplementowanej funkcji.


class Node:
    def __init__(self):
        self.value = None
        self.next = None


def insertion_sort(f):
    if f == None:
        return None
    sortedlist = f
    f = f.next
    sortedlist.next = None
    while f != None:
        curr = f
        f = f.next
        if curr.key < sortedlist.value:
            curr.next = sortedlist
            sortedlist = curr
        else:
            search = sortedlist
            while search.next != None and curr.key > search.next.key:
                search = search.next
            curr.next = search.next
            search.next = curr
    return sortedlist


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


def bucketsort(L):
    n = 0
    tmp = L
    while tmp != None:
        tmp = tmp.next
        n += 1

    section = 10 / n
    tab = [Node() for _ in range(n)]  # tablica wiaderek
    p = L
    while p:
        idx = int(p.value / section)
        tmp = tab[idx]
        while tmp.next != None:
            tmp = tmp.next
        tmp.next = Node()
        tmp.next.value = p.value
        p = p.next

    for i in range(len(tab)):
        if tab[i].next != None:
            tab[i] = insertion_sort(tab[i].next)

    first = tab[0]
    p = first
    for i in range(1, len(tab)):
        if tab[i].value != None:
            while p.next != None:
                p = p.next
            p.next = tab[i]
            p = p.next

    return first

    first = tab[0]
    p = first
    for i in range(len(tab)):
        if tab[i] != None:
            while p != None:
                p = p.next
            p.next = tab[i]
            p = p.next

    return first


A = [0, 1, 3, 2, 5, 5, 1.22, 3.44, 4.51, 4.12]
A = tab2list(A)
printlist(A)
A = bucketsort(A)
printlist(A)
