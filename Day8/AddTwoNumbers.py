# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = l1
        temp2 = l2
        num1 = ""
        num2 = ""
        while temp1:
            num1+=str(temp1.val)
            temp1=temp1.next
        num1 = int(num1[::-1])
        while temp2:
            num2+=str(temp2.val)
            temp2=temp2.next
        num2 = int(num2[::-1])
        num = str(num1+num2)[::-1]
        head = ListNode(int(num[0]))
        current = head
        for i in num[1:]:
            current.next = ListNode(int(i))
            current = current.next
        return head