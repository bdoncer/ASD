class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

def all_paths(root,res= []):
    if root.left == None and root.right == None:
        res = res + [root.key]
        print(res)
    if root.right != None:
        all_paths(root.right,res+[root.key])
    if root.left != None:
        all_paths(root.left, res + [root.key])


x = Node(1)
y = Node(2)
z = Node(3)
a = Node(4)
b = Node(5)
c = Node(6)
d = Node(7)
e = Node(8)
x.left = y
y.left = z
x.right = a
a.right = b
a.left = c
c.right = e
c.left = d
print(all_paths(x))