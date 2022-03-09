class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
def balanced_BST(T):
    T = sorted(T)
    middle = (len(T)-1)//2
    x = Node(T[middle])
    make_BST(T,0,middle-1,x)
    make_BST(T,middle+1,len(T)-1, x)
    return x
def make_BST(T,left,right,where):
    if left > right:
        return
    middle = left+(right-left)//2
    x = Node(T[middle])
    if x.key > where.key:
        where.right = x
        x.parent = where
    else:
        where.left = x
        x.parent = where
    make_BST(T,left,middle-1,x)
    make_BST(T,middle+1,right,x)



