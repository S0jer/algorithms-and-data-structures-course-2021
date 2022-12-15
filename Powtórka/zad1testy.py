# zad1testy.py

from math import log2, floor

TESTS = [
    [5, 11, 17, 13, 2, 7, 3],
    [5, 11, 17, 13, 2, 7, 3, 19],
    [1, 2, 3, 4, 5, 6, 7],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    [8, 7, 6, 5, 4, 3, 2, 1, 9, 10, 11, 12, 13, 14, 15],
    [5, 6, 7, 8, 4, 3, 2, 1],
    [25, 26, 27, 20, 15, 10, 17, 23, 22, 24],
    [10, 100, 1000, 9, 90, 99, 999],
    [1, 10, 20, 40, 30, 28, 32, 50, 45, 55]
]


class Node:
    def __init__(self):
        self.left = None  # lewe podrzewo
        self.right = None  # prawe poddrzewo
        self.parent = None  # rodzic drzewa jesli istnieje
        self.key = None  # przechowywana wartosc


def CreateBST(l):
    def InsertToBST(p, val):
        t = Node()
        t.key = val
        if p is None: return t

        r = p
        while r is not None:
            q = r
            if val < r.key:
                r = r.left
            else:
                r = r.right

        if val < q.key:
            q.left = t
        else:
            q.right = t

        t.parent = q
        return p

    p = None
    for val in l: p = InsertToBST(p, val)
    return p


def PrintTree(root, key="key", left="left", right="right"):
    def display(root, key=key, left=left, right=right):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if getattr(root, right) is None and getattr(root, left) is None:
            line = '%s' % getattr(root, key)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if getattr(root, right) is None:
            lines, n, p, x = display(getattr(root, left))
            s = '%s' % getattr(root, key)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if getattr(root, left) is None:
            lines, n, p, x = display(getattr(root, right))
            s = '%s' % getattr(root, key)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = display(getattr(root, left))
        right, m, q, y = display(getattr(root, right))
        s = '%s' % getattr(root, key)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    lines, *_ = display(root, key, left, right)
    for line in lines:
        print(line)


def Size(p):
    return 0 if p is None else Size(p.left) + Size(p.right) + 1


def Hight(p):
    return 0 if p is None else max(Hight(p.left), Hight(p.right)) + 1


def Tree2Set(p):
    def rek(p):
        nonlocal zb

        if p is not None:
            zb.add(p.key)
            rek(p.left)
            rek(p.right)

    zb = set()
    rek(p)
    return zb


def CheckTree(p):
    def rek(p, n=0):
        nonlocal min_level
        nonlocal max_level

        if p is not None:
            min_level[n] = min(min_level[n], p.key)
            max_level[n] = max(max_level[n], p.key)

            rek(p.left, n + 1)
            rek(p.right, n + 1)

    h = Hight(p)
    min_level = [999 for _ in range(h)]
    max_level = [0 for _ in range(h)]
    rek(p)
    # print(min_level)
    # print(max_level)
    for i in range(1, h):
        if min_level[i] <= max_level[i - 1]: return False
    return True


def CheckParents(p):
    if p is None: return True
    if p.left is not None:
        if p.left.parent != p: return False
    if p.right is not None:
        if p.right.parent != p: return False
    return CheckParents(p.left) and CheckParents(p.right)


def CheckResult(bst, result):
    if Size(result) != Size(bst): return False  # kontrola rozmiarow
    if Hight(result) != floor(log2(Size(bst)) + 1): return False  # kontrola wysokosci
    if Tree2Set(result) != Tree2Set(bst): return False  # porównanie zawartosci
    if not CheckTree(result): return False  # varunek poziomow
    if not CheckParents(result): return False  # kontrola parentow
    return True


def runtests(f):
    OK = True
    for d in TESTS:
        print("--------")
        print("dane = ", d)

        bst = CreateBST(d)
        print("BST  = ", end='')
        PrintTree(bst)
        print()

        result = f(bst)

        print("Res  = ", end='')
        PrintTree(result)
        print()

        if CheckResult(CreateBST(d), result):
            print("OK")
        else:
            print("Error")
            OK = False

    print()
    if OK:
        print("Passed all tests")
    else:
        print("Failed")
