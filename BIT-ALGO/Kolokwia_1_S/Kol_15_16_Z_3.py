# 3. Dana jest struktura Node opisująca listę jednokierunkową:
# struct Node { Node * next; int value; };
# Proszę zaimplementować funkcję Node* fixSortedList( Node* L ), która otrzymuje na
# wejściu listę jednokierunkową bez wartowanika. Lista ta jest prawie posortowana w tym sensie, że
# powstała z listy posortowanej przez zmianę jednego losowo wybranego elementu na losową
# wartość. Funkcja powinna przepiąć elementy listy tak, by lista stała się posortowana i zwrócić
# wskaźnik do głowy tej listy. Można założyć, że wszystkie liczby na liście są różne i że lista ma co
# najmniej dwa elementy. Funkcja powinna działać w czasie liniowym względem długości listy
# wejściowej.

class Node():
    def __init__(self):
        self.next = None
        self.value = None


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


def fixSortedList(head):
    p = head
    while p.next:
        prev = p
        p = p.next
        if p.next.key < p.value and prev.value < p.value:
            tmp = Node()
            tmp.value = p.next.key
            std = Node()
            std.value = p.value
            prev.next = p.next.next
            break
    if std.value < head.key:
        std.next = head
        head = std
    if tmp.value < head.value:
        tmp.next = head
        head = tmp
    # while p.next and p.value < n:
    #     printlist(head)
    #     prev = p
    #     p = p.next
    #     if prev.value < std.value and std.value < p.value:
    #         prev.next = std
    #         std.next = p
    #     elif prev.value < std.value and p.next is None:
    #         p.next = std
    #     if prev.value < tmp.value and tmp.value < p.value:
    #         prev.next = tmp
    #         tmp.next = p
    #     elif prev.value < tmp.value and p.next is None:
    #         p.next = tmp
    p = head
    while p.next:
        prev = p
        p = p.next
        if prev.value < std.value and std.value < p.key:
            prev.next = std
            std.next = p
            break
        elif prev.value < std.value and p.next is None:
            p.next = std
            break
    p = head
    while p.next:
        prev = p
        p = p.next
        if prev.value < tmp.value and tmp.value < p.value:
            prev.next = tmp
            tmp.next = p
            break
        elif prev.value < tmp.value and p.next is None:
            p.next = tmp
            break
    return head


if __name__ == '__main__':
    head = tab2list([1, 3, 4, 8, 5, 6, 7])
    printlist(head)
    head = fixSortedList(head)
    printlist(head)
