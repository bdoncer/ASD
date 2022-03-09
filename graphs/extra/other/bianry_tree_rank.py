class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        self.rank = 0
def ranks(root):
    res = 0
    if root.left == None and root.right == None:
        root.rank = 1
        return 1
    if root.right != None:
        res = ranks(root.right)+1
    if root.left != None:
        res = max(res,ranks(root.left)+1)
    root.rank = res
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
print(ranks(c))