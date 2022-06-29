# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        s = 0
        temp = head
        while temp:
            s = s*2 + int(temp.val)
            temp = temp.next
        return s