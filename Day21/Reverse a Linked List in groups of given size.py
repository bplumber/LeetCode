"""Return reference of new head of the reverse linked list
  The input list will have at least one element
  Node is defined as

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
  This is method only submission.
  You only need to complete the method.
"""
class Solution:
    def reverse(self,head, k):
        cur = head
        prev = None
        temp = None
        ct = 0
       
        while cur and ct < k:
           temp = cur.next
           cur.next = prev
           prev = cur
           cur = temp
           ct +=1
        if temp != None:
           head.next = self.reverse(temp, k)
        return prev