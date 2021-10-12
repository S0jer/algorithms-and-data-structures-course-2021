# Zadanie 1. Proszę zaimplementować:
# 1. Scalanie dwóch posortowanych list jednokierunkowych do jednej.
# 2. Algorytm sortowania list jednokierunkowych przez scalanie serii naturalnych.
# 3. Co się stanie, jeśli w powyższym algorytmie będziemy łączyć poprzednio posortowaną listę z kolejną,
# zamiast łączenia dwóch kolejnych list?

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def print_list(p):
    arr = []
    while p is not None:
        arr.append(p.val)
        p = p.next
    print(arr)


def list_to_node(l):
    head = Node(None, None)
    curr = head
    for el in l:
        curr.next = Node(el, None)
        curr = curr.next
    return head


def find(head):
    if head.next is None:
        return None
    head = head.next
    while head.next is not None and head.val <= head.next.val:
        head = head.next
    H = head.next
    head.next = None
    x = Node(None, None)
    x.next = H
    return x


def sort_nat(L):
    if L is None:
        return None
    tail = find(L.next)
    S = L
    L = tail
    while L.next is not None and tail.next is not None:
        tail = find(L)
        S = scal(S, L)
        L = tail
    return S

def scal(head_1, head_2):
    if head_1 is None or head_1.next is None:
        return head_2
    if head_2 is None or head_2.next is None:
        return head_1
    prev_1 = head_1
    curr_1 = head_1.next
    prev_2 = head_2
    curr_2 = head_2.next
    while curr_1 and curr_2:
        if curr_1.val >= curr_2.val:
            std = Node(curr_2.val)
            prev_1.next = std
            std.next = curr_1
            prev_1 = prev_1.next
            prev_2 = prev_2.next
            curr_2 = curr_2.next
        else:
            prev_1 = prev_1.next
            curr_1 = curr_1.next
    if curr_2 is not None and prev_1 is not None:
        prev_1.next = curr_2
    while curr_1 is not None and curr_1.next is not None:
        curr_1 = curr_1.next
    return head_1


if __name__ == '__main__':
    # head = list_to_node([1, 3, 5, 2, 7, 10, 9, 8, 31, 37, 40])
    # print_list(head)
    # head = sort_nat(head)
    # print_list(head)

    head_1 = list_to_node([8, 9, 31, 37, 40]) # , 13, 45, 60, 88, 92])
    head_2 = list_to_node([1, 9]) # , 6, 47, 50, 71, 90, 91, 93])
    print_list(head_2)
    head = scal(head_1, head_2)
    print_list(head)
