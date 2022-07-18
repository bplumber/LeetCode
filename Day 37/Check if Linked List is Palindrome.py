class Solution:
    def isPalindrome(self, head):
        def rev(head):
            prev = None
            cur = head
            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev
    
        def md(head):
            s, f = head, head.next
            while f and f.next:
                s, f = s.next, f.next.next
            return s
        
        if head.next==None:
            return 1
        mid = md(head)
        temp = mid.next
        mid.next = rev(temp)
        fromHead = head
        fromMiddle = mid.next
        while fromMiddle:
            if fromMiddle.data!=fromHead.data:
                return 0
            fromMiddle, fromHead = fromMiddle.next, fromHead.next
        return 1