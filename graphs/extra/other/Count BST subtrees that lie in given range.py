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

def main(root,minn,maxx):
    def subtrees(root):
        nonlocal ctr
        if root.key < minn or root.key > maxx:
            if root.left != None:
                subtrees(root.left)
            if root.right != None:
                subtrees(root.right)
            return False
        if root.left == None and root.right == None:
            ctr += 1
            return True
        one = True
        two = True
        if root.right != None:
            one = subtrees(root.right)
        if root.left != None:
            two = subtrees(root.left)
        if one == True and two == True:
            ctr += 1
            return True
        else:
            return False

    ctr = 0
    subtrees(root)
    return ctr

a = Node(10)
insert(a,50)
insert(a,5)
insert(a,1)
insert(a,40)
insert(a,100)
print(main(a,1,45))
