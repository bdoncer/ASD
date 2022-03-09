'''Dana jestr struktura opisująca listę jednokierunkową dla liczb rzeczywistych:
struct Node{ Node* next; double value; }
Proszę zaimplementować funkcję void Sort( Node* list ), która otrzymuje na wejściu listę
liczb rzeczywistych (z wartownikiem), wygenerowaną zgodnie z rozkładem jednostajnym na
przedziale [0,10) i sortuje jej zawartość w kolejności niemalejącej. Funkcja powinna być możliwie
jak najszybsza (biorąc pod uwagę warunki zadania). Proszę oszacować złożoność
zaimplementowanej funkcji.
'''
from math import floor


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


def sort(p):
    head = p
    length = -1
    while p != None:
        length += 1
        p = p.next
    p = head.next
    wartownicy = [0] * length
    lasty = [0] * length
    for i in range(len(wartownicy)):
        a = Node(-1)
        wartownicy[i] = a
    for i in range(len(wartownicy)):
        a = Node(-1)
        lasty[i] = a
    while p != None:
        q = p.next
        p.next = None
        if lasty[floor(p.val * length / 10)].val == -1:
            wartownicy[floor(p.val * length / 10)].next = p
            lasty[floor(p.val * length / 10)] = p
        else:
            lasty[floor(p.val * length / 10)].next = p
            lasty[floor(p.val * length / 10)] = p
        p = q

    for i in range(len(wartownicy)):
        if wartownicy[i].next != None:
            wartownicy[i].next,lasty[i] = InsertSort_lists(wartownicy[i].next)

    k = 0
    while wartownicy[k].next == None:
        k += 1
    last_changed = k
    for i in range(k+1,len(wartownicy)):
        if lasty[i].val != -1:
            lasty[last_changed].next = wartownicy[i].next
            last_changed = i
    return wartownicy[k].next


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


T = [0.9, 6, 3, 0.8, 9,5,8,3,5,2,3,5,8,5,9,1,5,7]
q = arr_to_list(T)
WARTOWNIK = Node(-999)
WARTOWNIK.next = q
a = sort(WARTOWNIK)
print_list(a)
