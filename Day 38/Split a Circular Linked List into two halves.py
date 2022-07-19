class Solution:
    def splitList(self, head, head1, head2):
        chk = head
        temp = head.next
        ct = 1
        while chk!=temp:
            temp = temp.next
            ct+=1
        if ct%2!=0:
            firstlen = int(ct/2)+1
        else:
            firstlen = int(ct/2)
        secondlen = ct - firstlen
        head1 = head
        tpfirst = head1
        x = 0
        while x!=firstlen-1:
            tpfirst = tpfirst.next
            x+=1
        tpsecond = tpfirst.next
        head2 = tpsecond
        tpfirst.next = head1
        x = 0
        while x!=secondlen-1:
            tpsecond = tpsecond.next
            x+=1
        tpsecond.next = head2
        #this is to emulate pass by reference in python please don't delete below line.
        return head1,head2