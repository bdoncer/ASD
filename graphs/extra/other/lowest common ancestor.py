def lowest(val1,val2,root):
    while True:
        if root.val > val1 and root.val > val2:
            root = root.left
        elif root.val < val1 and root.val < val2:
            root = root.right
        elif root.val > val1 and root.val < val2:
            return root
