class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def merge(p1,p2):
    head = Node(-999)
    last = head
    while p1 != None and p2 != None:
        if p1.val < p2.val:
            last.next = p1
            last = p1
            p1 = p1.next
        else:
            last.next = p2
            last = p2
            p2 = p2.next
    while p1!= None:
        last.next = p1
        last = p1
        p1 = p1.next
    while p2 != None:
        last.next = p2
        last = p2
        p2 = p2.next
    return head.next



def MergeSort(p):
    head = p
    dlugosc = 0
    while p != None:
        dlugosc += 1
        p = p.next
    if dlugosc == 1:
        return head
    i = 0
    p = head
    while i < (dlugosc//2)-1:
        p = p.next
        i += 1
    head2 = p.next
    p.next = None
    left = MergeSort(head)
    right = MergeSort(head2)
    x = merge(left,right)
    return x


def arr_to_list(arr):
    list_head = None
    list_tail = None
    for value in arr:
        if list_head is None:
            list_head = Node(value)
            list_tail = list_head
            continue
        list_tail.next = Node(value)
        list_tail = list_tail.next

    return list_head


def print_list(list):
    tmp = list
    while tmp is not None:
        print(tmp.val, end=" ", sep=" ")
        tmp = tmp.next
    print("")

T = [4,7,33,232,1111,4,6,99,1234,123456]
head = arr_to_list(T)
cos = MergeSort(head)
print_list(cos)
