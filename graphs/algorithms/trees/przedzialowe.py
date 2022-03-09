#takie co sumuje z tablicy
from queue import Queue
class Node:
    def __init__(self):
        self.sum = 0
        self.przedzial = None
        self.left = None
        self.right = None
        self.parent = None
def sumaaa(T):
    n = len(T)
    Q = Queue()
    for i in range(n):
        x = Node()
        x.sum = T[i]
        Q.put(x)
    while Q.qsize() > 1:
        left = Q.get()
        right = Q.get()
        x = Node()
        x.sum = left.sum+right.sum
        left.parent = x
        right.parent = x
        x.left = left
        x.right = right
        Q.put(x)
        root = x
    przedzial(root,0,n-1)
    return root
from math import floor,ceil
def przedzial(root,minn,maxx):
    middle = minn+(maxx-minn)/2
    root.przedzial = [minn,maxx]
    if root.right != None:
        przedzial(root.right,ceil(middle),maxx)
    if root.left != None:
        przedzial(root.left,minn,floor(middle))


def print_tree(root):
    if root.right != None:
        print_tree(root.right)
    if root.left != None:
        print_tree(root.left)
    print(root.sum,root.przedzial)

T = [0,3,5,1]
k = sumaaa(T)
print_tree(k)




