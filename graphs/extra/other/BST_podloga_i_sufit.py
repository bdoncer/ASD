class BSTNode:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

def floor_ceil(root, key):
    floor = None
    ceil = None
    while root != None:
        if root.key == key:
            floor = root
            ceil = root
            break
        elif key < root.key:
            ceil = root
            root = root.left
        else:
            floor = root
            root = root.right

    return floor, ceil


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

x = BSTNode(10)
a = insert(x, 7)
b = insert(x, 15)
c = insert(x, 1)
d = insert(x, 6)
e = insert(x, 11)
f = insert(x, 8)
g = insert(x, 18)
fl,ce = floor_ceil(x,14)
print(fl.key,ce.key)