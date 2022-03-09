class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
from math import inf
def is_BST(p,min,max):
    if p == None:
         a = 2
    else:
        if p.key >= max or p.key <= min:
            return False
        if p.left != None:
            return is_BST(p.left,min,p.key)
        if p.right != None:
            return is_BST(p,p.key,max)
    return True


def main(p):
    x = is_BST(p.left,-inf,p.key)
    y = is_BST(p.right,p.key,inf)
    print(x)
    print(y)


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

x = Node(12)
z = Node(20)
k = Node(28)
c = Node(5)
x.left = c
x.right = z
z.left = k
main(x)