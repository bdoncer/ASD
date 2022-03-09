class Node:
    def __init__(self,key):
        self.key = key
        self.sum = 0
        self.left = None
        self.right = None

def suma(root):
    res = 0
    if root.left == None and root.right == None:
        root.sum = root.key
        return 0
    if root.left != None:
        res += suma(root.left)
        res += root.left.key
    if root.right != None:
        res +=suma(root.right)
        res += root.right.key
    root.sum = res
    return res

def czy_sum_tree(root):
    suma(root)
    x = True
    y = True
    if root.key != root.sum:
        return False
    if root.left != None:
        x = czy_sum_tree(root.left)
    if root.right != None:
        y = czy_sum_tree(root.right)
    if x == False or y == False:
        return False
    return True


x = Node(44)
y = Node(9)
z = Node(4)
t = Node(5)
a = Node(13)
b = Node(6)
c = Node(7)
x.left = y
y.left = z
y.right = t
x.right = a
a.right = b
a.left = c
print(czy_sum_tree(x))