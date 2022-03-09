
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def InsertSort_lists(p):
    if p == None:
        return p
    wartownik = Node(-999)
    wartownik.next = p
    prev = wartownik
    p = wartownik.next
    while p != None:
        if prev.val <= p.val:
            prev = p
            p = p.next
        else:
            q_prev = wartownik
            q = wartownik.next
            prev.next = p.next
            while q.val < p.val:
                q_prev = q
                q = q.next
            p.next = q
            q_prev.next = p
            p = prev.next
    return wartownik.next,prev