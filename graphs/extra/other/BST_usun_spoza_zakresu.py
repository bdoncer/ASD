class BSTNode:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

def zakres(root, min, max):
    if root == None:
        return root
    root.left = zakres(root.left, min, max)
    root.right = zakres(root.right, min, max)
    if root.key < min:
        root = root.right
    elif root.key > max:
        root = root.left
    return root


def insert(root, key):
    while True:
        if root.key < key:
            if root.right == None:
                x = BSTNode(key)
                root.right = x
                x.parent = root
                break
            else:
                root = root.right
        if root.key > key:
            if root.left == None:
                x = BSTNode(key)
                root.left = x
                x.parent = root
                break
            else:
                root = root.left
    return x

def print_tree(root, val="key", left="left", right="right"):
    def display(root, val=val, left=left, right=right):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if getattr(root, right) is None and getattr(root, left) is None:
            line = '%s' % getattr(root, val)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if getattr(root, right) is None:
            lines, n, p, x = display(getattr(root, left))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if getattr(root, left) is None:
            lines, n, p, x = display(getattr(root, right))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = display(getattr(root, left))
        right, m, q, y = display(getattr(root, right))
        s = '%s' % getattr(root, val)
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

    lines, *_ = display(root, val, left, right)
    for line in lines:
        print(line)
x = BSTNode(10)
a = insert(x, 7)
b = insert(x, 15)
c = insert(x, 1)
d = insert(x, 6)
e = insert(x, 11)
f = insert(x, 8)
g = insert(x, 18)
k = zakres(x,9,100)
print_tree(k)