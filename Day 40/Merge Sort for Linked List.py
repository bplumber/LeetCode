class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data            
        self.next = None

class Solution:
    #Function to sort the given linked list using Merge Sort.
    def mergeSort(self, head):
        
        def md(head):
            s = head
            f = head.next
            while f and f.next:
                f = f.next.next
                s = s.next
            return s
        
        def merge(head):
            if head == None or head.next == None:
                return head
            m = md(head)
            l = head
            r = m.next
            m.next = None
            l = merge(l)
            r = merge(r)
            temp = Node(1)
            headd = temp
            while l and r:
                if l.data>r.data:
                    temp.next = r
                    r = r.next
                    temp = temp.next
                else:
                    temp.next = l
                    l = l.next
                    temp = temp.next
            if l:
                temp.next = l
                l = l.next
                temp = temp.next
            if r:
                temp.next = r
                r = r.next
                temp = temp.next
            return headd.next
        
        return merge(head)