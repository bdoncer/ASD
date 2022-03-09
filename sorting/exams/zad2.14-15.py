'''Dane są następujące struktury:
struct Node { Node* next; int val; };
struct TwoLists { Node* even; Node* odd; };
Napisać funkcję: TwoLists split(Node* list);
Funkcja rozdziela listę na dwie: jedną zawierającą liczby parzyste i drugą zawierającą liczby
nieparzyste. Listy nie zawierają wartowników.'''


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def odd_and_even(p):
    head_odd = Node(-1)
    head_even = Node(-1)
    head_even.next = p
    prev = head_even
    p_odd = head_odd
    while p != None:
        if p.val % 2 == 0:
            prev.next = p.next
            p.next = None
            p_odd.next = p
            p_odd = p
            p = prev.next
        else:
            prev = p
            p = p.next
    return head_odd.next,head_even.next


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

T = [2,1,4,2,5,7,4,7,3,7,4,6,4,7,4,8,9]
k = arr_to_list(T)
a,b = odd_and_even(k)
print_list(a)
print_list(b)