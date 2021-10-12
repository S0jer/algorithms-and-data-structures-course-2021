# 2. Dane są następujące struktury:
# struct Node { Node* next; int val; };
# struct TwoLists { Node* even; Node* odd; };
# Napisać funkcję: TwoLists split(Node* list);
# Funkcja rozdziela listę na dwie: jedną zawierającą liczby parzyste i drugą zawierającą liczby
# nieparzyste. Listy nie zawierają wartowników.

class Node:
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


def TwoLists(head):
    if head is None or head.next is None:
        return head
    even = Node()
    e = even
    odd = Node()
    o = odd
    prev = head
    while prev:
        if prev.value % 2 == 0:
            even.next = Node()
            even.next.value = prev.value
            even = even.next
        else:
            odd.next = Node()
            odd.next.value = prev.value
            odd = odd.next
        prev = prev.next
    return e.next, o.next


head = tab2list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
even, odd = TwoLists(head)
printlist(even)
printlist(odd)
