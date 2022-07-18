def isCircular(head):
    f, s = head, head
    while f and f.next:
        f, s =f.next.next, s.next
        if f == s:
            return 1
    return 0 