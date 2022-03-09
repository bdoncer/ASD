class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
def wstaw_do_posortowanej(p,wart):
    prev = wart
    k = wart.next
    while k != None and k.val <= p.val:
        prev = k
        k = k.next
    prev.next = p
    p.next = k
def sort(p):
    wart = Node(-1)
    wart.next = p
    prev = p
    p = p.next
    q = p.next
    while q != None:
        if p.val > prev.val and p.val < q.val:
            sem = 0
        else:
            break
        prev = p
        p = q
        q = q.next
    #trzeba sprawdzic czy to p czy q jest zle
    p.next = None
    prev.next = q
    wstaw_do_posortowanej(p,wart)
    '''if sem == 0:
        kp = wart
        k = wart.next
        while k != None and k.val > p.val:
            kp = k
            k = k.next
        kp.next = p
        p.next = k
    if sem == 1:
        kp = prev
        k = p
        while k.val <= p.val:
            kp = k
            k = k.next
            if k == None:
                prev.next = q
                kp.next = p
                p.next = None
                break
        prev.next = k
        tmp = k.next
        k.next = p
        p.next = tmp'''
    return wart.next

def print_list(p):
    while p != None:
        print(p.val)
        p = p.next
def tab_to_list(T):
    prev = Node(T[0])
    first = prev
    for i in range(1,len(T)):
        p = Node(T[i])
        prev.next = p
        prev = p
        p = p.next
    return first

T=[1,2,3,4,7,9,12,5]
a = tab_to_list(T)
k = sort(a)
print_list(k)



