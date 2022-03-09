class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

def insert(p,value):
    x = Node(value)
    while True:
        if value < p.key:
            if p.left == None:
                p.left = x
                x.parent = p
                return
            p = p.left
        elif value > p.key:
            if p.right == None:
                p.right = x
                x.parent = p
                return
            p = p.right


def minimum(root):
    while root.left != None:
        root = root.left
    return root

def maximum(root):
    while root.right != None:
        root = root.right
    return root

def nastepnik(root):
    if root.right != None:
        return minimum(root.right)
    if root.right == None:
        while root.parent != None and  root.parent.key < root.key:
            root = root.parent
        return root.parent
    if root.parent == None:
        return None

def poprzednik(root):
    if root.left != None:
        return maximum(root.left)
    if root.left == None:
        while root.parent != None and  root.parent.key > root.key:
            root = root.parent
        return root.parent
    if root.parent == None:
        return None



#wracam z lewa - ide w prawo, wracam z prawa - ide w gore,wracam z dolu - ide w lewo
def morris(root):
    while root != None:
        #nie ma lewego dziecka
        if root.left == None:
            print(root.key)
            root = root.right
        #jest lewe dziecko
        else:
            prev = root.left
            while prev.right != None and prev.right != root:
                prev = prev.right
            if prev.right == None:
                prev.right = root
                root = root.left
            else:
                print(root.key)
                prev.right = None
                root = root.right

#wracam z lewa - ide w prawo, wracam z prawa - ide w gore,wracam z dolu - ide w lewo
def morris_2(root):
    czy_zwiedzone_lewo = False
    while root != None:
        if czy_zwiedzone_lewo == False:
            root = minimum(root)
        print(root.key)
        czy_zwiedzone_lewo = True
        if root.right != None:
            czy_zwiedzone_lewo = False
            root = root.right
        elif root.parent != None:
            while root.parent != None and root == root.parent.right:
                root = root.parent
            if root.parent == None:
                break
            root = root.parent
        else:
            break


def search(p,value):
    if p == None:
        return 'Not exist'
    if p.key == value:
        return p
    if p.key < value:
        return search(p.right,value)
    if p.key > value:
        return search(p.left,value)

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


a = Node(10)
b = Node(13)
c = Node(5)
d = Node(4)
e = Node(6)
insert(a,13)
insert(a,5)
insert(a,4)
insert(a,6)
print_tree(a)
'''a.left =c
a.right =b
c.left = d
c.right = e'''
morris(a)