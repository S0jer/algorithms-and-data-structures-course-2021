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


def remove(root, key):
    while root is not None:

        val = root.key

        if root.left is None and key < val:
            return False

        elif root.right is None and key > val:
            return False

        elif key == val:

            if root.left is not None and root.right is None:
                if root.parent.left == root:
                    root.parent.left = root.left
                else:
                    root.parent.right = root.left

            elif root.right is not None and root.left is None:
                if root.parent.left == root:
                    root.parent.left = root.right
                else:
                    root.parent.right = root.right

            elif root.right is not None and root.left is not None:
                cnt = nast(root)
                if cnt.parent.left == cnt:
                    cnt.parent.left = None
                else:
                    cnt.parent.right = None

                root.key = cnt.key

            return True

        elif key > val:
            root = root.right

        elif key < val:
            root = root.left


def nast(root):
    if root.right is not None:
        root = root.right

        while root.left is not None:
            root = root.left

        return root

    elif root.parent is not None:
        p_root = root.parent
        while p_root.parent is not None:
            if p_root.right != root:
                return p_root
            root = p_root
            p_root = p_root.parent

        return None

    return None


def poprzed(root):
    if root.left is not None:
        root = root.left

        while root.right is not None:
            root = root.right

        return root

    elif root.parent is not None:
        p_root = root.parent
        while p_root.parent is not None:
            if p_root.left != root:
                return p_root
            root = p_root
            p_root = p_root.parent

        return None

    return None


def find_idx(root, idx):

    if root.left is not None and root.left.key == idx:
        root = root.left

        while root.right is not None:
            root = root.right

        return root

    elif root.left is not None and root.left.key > idx:
        return find_idx(root.left, idx)

    elif root.left is not None and idx > root.left.key:
        if idx - root.left.key > 1:
            idx = idx - root.left.key - 1
            return find_idx(root.right, idx)
        else:
            return root

if __name__ == '__main__':
    root = BSTNode(10)
    insert(root, -5)
    insert(root, -6)
    insert(root, -7)
    insert(root, 1)
    insert(root, 12)
    insert(root, 11)
    print_tree(root)

