class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

def wysokosc(root):
    res = 1
    if root.left == None and root.right == None:
        return 1
    if root.left != None:
        res = max(res,1+wysokosc(root.left))
    if root.right != None:
        res = max(res,1+wysokosc(root.right))
    return res


x = Node(1)
y = Node(1)
z = Node(1)
a = Node(1)
b = Node(1)
c = Node(1)
x.left = y
y.left = z
x.right = a
a.right = b
b.left = c
print(wysokosc(x))