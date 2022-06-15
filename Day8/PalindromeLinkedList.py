# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp  = head
        lt = []
        while temp:
            lt.append(temp.val)
            temp = temp.next
        return lt == lt[::-1]