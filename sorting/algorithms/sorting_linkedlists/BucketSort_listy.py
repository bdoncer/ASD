#index = floor(((array[i]-mini)*n)/(maxi-mini+1))


class Node:
    def __init__(self,val):
        self.next = None
        self.val = val
from math import inf,floor
def SelectSort(p):
    wartownik = Node(-1)
    wartownik.next = p
    prev = wartownik
    while p != None:
        #szukam minimum
        prev_q = prev
        q = p
        res = inf
        minn = -1
        prev_min = -1
        while q != None:
            if q.val < res:
                res = q.val
                minn = q
                prev_min = prev_q
            prev_q = q
            q = q.next
        if minn == p:
            prev = p
            p = p.next
        else:
            prev.next = minn
            prev_min.next = minn.next
            minn.next = p
            prev = minn
    return wartownik.next


def BucketSort(p,a,b):
    lengh = 0
    first = p
    while p != None:
        lengh += 1
        p = p.next
    wartownicy = []
    lasty = []
    for i in range(lengh):
        x = Node(-1)
        wartownicy.append(x)
        lasty.append(x)
    p = first
    while p != None:
        index = floor(((p.val - a) * lengh) / (b - a + 1))
        next_p = p.next
        lasty[index].next = p
        p.next = None
        lasty[index] = p
        p = next_p
    for i in range(lengh):
        wartownicy[i] = SelectSort(wartownicy[i])
    head = Node(-1)
    p  = head
    for i in range(lengh):
        wartownicy[i] = wartownicy[i].next
        while wartownicy[i] != None:
            p.next = wartownicy[i]
            wartownicy[i] = wartownicy[i].next
            p = p.next
    return head.next










def arr_to_list(arr):
    list_head = None
    list_tail = None
    for val in arr:
        if list_head is None:
            list_head = Node(val)
            list_tail = list_head
            continue
        list_tail.next = Node(val)
        list_tail = list_tail.next

    return list_head


def print_list(list):
    tmp = list
    while tmp is not None:
        print(tmp.val, end=" ", sep=" ")
        tmp = tmp.next
    print("")

T = [0,4,34,6,3,43,4,2,5,33,532,324,234,4324,32,324]
x = arr_to_list(T)
k = BucketSort(x,0,4324)
print_list(k)
