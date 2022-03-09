class Node:
    def __init__(self, val):
        self.key = val
        self.left = None
        self.right = None


def transform(root):
    def rec(root):
        nonlocal sum
        if (root == None):
            return
        rec(root.right)
        sum = sum + root.key
        root.key = sum - root.key
        rec(root.left)
    sum = 0
    rec(root)


def printInorder(root):
    if (root == None):
        return

    printInorder(root.left)
    print(root.key)
    printInorder(root.right)
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

a = Node(10)
insert(a,50)
insert(a,5)
insert(a,1)
insert(a,40)
insert(a,100)
transform(a)
printInorder(a)