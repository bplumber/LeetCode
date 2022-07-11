# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tp = head
        x = 1
        count = 0
        while tp:
            tp = tp.next
            count+=1
        print(count)
        tp = head
        if x>(count-n):
            head = tp.next
            return head
        while(x<(count-n)):
            tp = tp.next
            x+=1
        if tp.next != None:
            tp.next = tp.next.next
        else:
            head = None
        return head