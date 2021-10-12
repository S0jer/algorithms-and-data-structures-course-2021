from zad1testy import runtests


class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.value = 1


def print_tree(root, key="key", left="left", right="right"):
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


def insert(root, key):
    val = root.key
    while val != key:

        if key < val and root.left == None:
            root.value += 1
            root.left = BSTNode(key)
            root.left.parent = root
            return True
        elif key < val:
            root.value += 1
            root = root.left

        elif key > val and root.right == None:
            root.value += 1
            root.right = BSTNode(key)
            root.right.parent = root
            return True
        elif key > val:
            root.value += 1
            root = root.right

        val = root.key

    return False


def ConvertTree(T):
    T_min = T
    T_max = T

    while T_min.left is not None:
        T_min = T_min.left
    while T_max.right is not None:
        T_max = T_max.right

    rot = BSTNode(T_min.key)

    while T_max != T_min:
        T_min = nast(T_min)
        insert_nT(rot, T_min.key)

    return rot


def nast(root):
    if root.right is not None:
        root = root.right

        while root.left is not None:
            root = root.left

        return root

    else:
        while root.parent is not None:
            if root.parent.right == root:
                root = root.parent
            else:
                return root.parent

    return None


def insert_nT(root, key):
    if not root:
        root = BSTNode(key)
        return
    Q = [root]

    while (len(Q)):
        root = Q[0]
        Q.pop(0)

        if not root.left:
            root.left = BSTNode(key)
            root.left.parent = root
            break
        else:
            Q.append(root.left)

        if not root.right:
            root.right = BSTNode(key)
            root.right.parent = root
            break
        else:
            Q.append(root.right)


runtests(ConvertTree)

root = BSTNode(10)
insert(root, 5)
insert(root, 4)
insert(root, 21)
insert(root, 15)
insert(root, 12)
insert(root, 25)
insert(root, 22)
insert(root, 23)
insert(root, 24)
insert(root, 27)
insert(root, 11)

result = ConvertTree(root)
