class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        s = head
        f = head 
        ct = 0
        while f and f.next:
            s = s.next
            f = f.next.next
            ct+=1
            if f == s:
                if s == head:
                    i = 0
                    while i < ct-1:
                        s = s.next
                        i+=1
                    s.next = None
                    break
                else:
                    s = head
                    while f.next != s.next:
                        s = s.next
                        f = f.next
                    f.next = None