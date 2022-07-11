# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p = head
        q = head
        try:
            while p and q:
                p = p.next
                q = q.next.next
                if p==q:
                    return True
        except:
            return False