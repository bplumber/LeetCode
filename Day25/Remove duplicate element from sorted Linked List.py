'''
	Your task is to remove duplicates from given 
	sorted linked list.
	
	Function Arguments: head (head of the given linked list) 
	Return Type: none, just remove the duplicates from the list.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
#Function to remove duplicates from sorted linked list.
def removeDuplicates(head):
    t1 = head
    t2 = head
    while t1:
        while t2 and t1.data == t2.data:
            t2 = t2.next
        t1.next = t2
        t1 = t1.next