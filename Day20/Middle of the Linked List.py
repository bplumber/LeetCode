# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: ListNode)-> ListNode:
        temp = head
        ct = 0 
        while temp:
            temp = temp.next
            ct+=1
        ct = int(ct/2) + 1
        tp = 0
        temp = head
        while temp:
            tp+=1
            if tp == ct:
                return temp
            temp = temp.next

# BETTER TORTOISE SOLUTION

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        f, s = head, head
        while f and f.next:
            f = f.next.next
            s = s.next
        return s