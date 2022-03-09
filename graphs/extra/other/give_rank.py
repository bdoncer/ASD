class BSTNode:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.rank = 0

def give_rank(root):
    if root.left == None and root.right == None:
        root.rank = 1
        return 1
    else:
        root.rank = 1
        if root.left != None:
            root.rank += give_rank(root.left)
        if root.right != None:
            root.rank += give_rank(root.right)
    return root.rank


