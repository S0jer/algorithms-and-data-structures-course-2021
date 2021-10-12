# Proszę napisać funkcję, która mając na wejściu ciąg tak zrealizowanych posortowanych list scala je
# w jedną posortowaną listę (składającą się z tych samych elementów).
# Przykład Dla tablicy [[0,1,2,4,5],[0,10,20],[5,15,25]] - po przekształceniu jej elementów
# z Python’owskich list na listy jednokierunkowe - wynikiem powinna być lista jednokierunkowa, która
# po przekształceniu jej na listę Python’owską przyjmie postać [0,0,1,2,4,5,5,10,15,20,25]


from zad3test import runtests

class Node:
    def __init__(self, val):
        self.next = None
        self.val = val


def merge(T):
    m, cnt = len(T), 0
    dp = [-1] * m

    for i in T:
        dp[cnt] = tab2list(i)
        cnt += 1

    check = 0
    result = Node(None)
    head = result
    while check < m:

        id_min = 0
        while dp[id_min] is None:
            id_min += 1

        for j in range(m):
            if dp[j] is not None and dp[id_min].val > dp[j].val:
                id_min = j

        next = dp[id_min]
        result.next = next

        if dp[id_min].next is None:
            check += 1

        dp[id_min] = dp[id_min].next
        result = result.next
        result.next = None

    return head.next


def tab2list(A):
    H = Node(A[0])
    C = H
    for i in range(1, len(A)):
        X = Node(A[i])
        X.value = A[i]
        C.next = X
        C = X
    return H


def printlist(L):
    while L != None:
        print(L.val, "->", end=" ")
        L = L.next
    print("|")

runtests( merge )

# T = [[0, 1, 2, 4, 5], [0, 10, 20], [5, 15, 25]]
#
# head = merge(T)
# printlist(head)
