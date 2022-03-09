class BSTNode:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.rank = 0
def ile_podwezlow(root):
    root.rank = 1
    if root.left != None:
        root.rank += ile_podwezlow(root.left)
    if root.right != None:
        root.rank += ile_podwezlow(root.right)
    return root.rank

def ity_najmniejszy(root,i):
    if root == None:
        return None
    ktory = 1
    if root.left != None:
        ktory = root.left.rank+1
    if ktory < i:
        return ity_najmniejszy(root.right,i-ktory)
    if ktory  == i:
        return root.key
    if ktory > i:
        return ity_najmniejszy(root.left,i)
def ile_wiekszych(root):
    ile = 0
    def licz(root):
        nonlocal ile
        ile += 1
        if root.left != None:
            licz(root.left)
        if root.right != None:
            licz(root.right)
    if root.left != None:
        licz(root.left)
    if root.right != None:
        licz(root.right)
    return ile

def ktory_w_drzewie(root):
    #jest korzeniem
    if root.parent == None:
        return root.left.rank+1
    #ma lewe dziecko i jest prawym dzieckiem
    if root.left != None and root.parent.right == root:
        return ktory_w_drzewie(root.parent)+root.left.rank+1
    #ma lewo dziecko i jest lewym dzieckiem
    if root.left != None and root.parent.left == root:
        return root.left.rank+1
    #nie ma lewego dziecka i jest prawym dzieckiem
    if root.left == None and root.parent.right == root:
        return ktory_w_drzewie(root.parent)+1
    #nie ma lewego dziecka i jest lewym dzieckiem
    if root.left == None and root.parent.left == root:
        return ktory_w_drzewie(root.parent)-ile_wiekszych(root)-1
        

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
h = ile_podwezlow(x)

print(ktory_w_drzewie())