'''3. Dana jest struktura Node opisująca listę jednokierunkową:
struct Node { Node * next; int value; };
Proszę zaimplementować funkcję Node* fixSortedList( Node* L ), która otrzymuje na
wejściu listę jednokierunkową bez wartowanika. Lista ta jest prawie posortowana w tym sensie, że
powstała z listy posortowanej przez zmianę jednego losowo wybranego elementu na losową
wartość. Funkcja powinna przepiąć elementy listy tak, by lista stała się posortowana i zwrócić
wskaźnik do głowy tej listy. Można założyć, że wszystkie liczby na liście są różne i że lista ma co
najmniej dwa elementy. Funkcja powinna działać w czasie liniowym względem długości listy
wejściowej.'''

class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
def find_wrong(p):
    head = Node(-100)
    prev_main = head
    head.next = p
    q = p.next
    while q != None:
        if p.val > q.val:
            if q.next == None:
                p.next = None
                prev = head
                p = head.next
                while q.val > p.val:
                    prev = p
                    p = p.next
                prev.next = q
                q.next = p
                break
            else:
                if p.val >= q.next.val:
                    prev_main.next = q
                    while q != None and p.val > q.val:
                        prev = q
                        q = q.next
                    prev.next = p
                    p.next = q
                    break
                else:
                    p.next = q.next
                    prev = p
                    p = head.next
                    while q.val > p.val:
                        prev = p
                        p = p.next
                    prev.next = q
                    q.next = p
                    break
        prev_main = p
        p = q
        q = q.next
    return head.next






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

T = [4,5,3,7]
q = arr_to_list(T)
x = find_wrong(q)
print_list(x)
