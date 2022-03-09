class Node:
    def __init__(self,val):
        self.next = None
        self.val = val
def reverse(p):
    if p == None:
        return None
    if p.next == None:
        return p
    prev = p
    p = p.next
    prev.next = None
    while p.next != None:
        q = p.next
        p.next = prev
        prev = p
        p = q
    p.next = prev
    return p
def print_list(p):
    while p != None:
        print(p.val)
        p = p.next
k = Node(1)
l = Node(2)
m = Node(3)
n = Node(4)
o = Node(5)
p = Node(6)




a = reverse(k)
print_list(a)



