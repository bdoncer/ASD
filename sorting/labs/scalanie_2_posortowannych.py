def merge_sorted(p1,p2):
    head = Node(-1)
    q = head
    while p1 != None and p2 != None:
        if p1.val <= p2.val:
            q.next = p1
            p1 = p1.next
        else:
            q.next = p2
            p2 = p2.next
        q = q.next

    if p1 == None:
        q.next = p2
    else:
        q.next = p1

    while q.next != None:
        q = q.next

    return head.next,q