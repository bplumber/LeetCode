

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None


class Solution:
    def addOne(self,head):
        temp = head
        lt = ""
        while temp:
            lt+=str(temp.data)
            temp=temp.next
        return Node(int(lt)+1)