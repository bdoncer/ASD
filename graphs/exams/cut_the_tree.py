class BNode:
    def __init__ (self,value):
        self.left = None
        self.right = None
        self.parent = None
        self.value = None

def cutthetree(root):
    res = 0
    if root.left == None and root.right == None:
        return root
    if root.left != None:
        while root.right == None and root.left != None:
            root = root.left
        if root.left != None and root.right != None:
            res += min(cutthetree(root.left),cutthetree(root.right),root.value)
        elif root.left == None and root.right == None:
            return root
        elif root.left == None and root.right != None:
            res += cutthetree(root)
    if root.right != None and root.right.value >= 0:
        return root.right.value
    return res
    '''if root.right != None and root.right.value < 0:
        res += cutthetree(root.right)
        while root.right == None and root.left != None:
            root = root.left
        if root.left != None and root.right != None:
            res += min(cutthetree(root.left),cutthetree(root.right),root.value)
        elif root.left == None and root.right == None:
            return root
        elif root.left == None and root.right != None:
            res += cutthetree(root)'''

