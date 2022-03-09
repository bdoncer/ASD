class Node:
    def __init__(self, val):
        self.key = val
        self.left = None
        self.right = None

def count(root):
    res1 = 0
    res2 = 0
    if root.left == None and root.right == None:
        return 1

    if root.left != None and root.left.left != None:
        res1+=count(root.left.left)
    if root.right != None and root.right.right != None:
        res1+=count(root.right.right)
    if root.left != None and root.left.right != None:
        res1+=count(root.left.right)
    if root.right != None and root.right.left != None:
        res1+=count(root.right.left)
    res1+=1
    if root.left != None:
        res2 += count(root.left)
    if root.right != None:
        res2 += count(root.right)
    return max(res1,res2)
def main(root):
    print(count(root))
root  = Node(10)
root.left = Node(20)
root.left.left = Node(40)
root.left.right = Node(50)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
root.right  = Node(22)
root.right.right = Node(25)
print(main(root))


