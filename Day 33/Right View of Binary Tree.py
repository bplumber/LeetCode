from collections import deque

class Solution:
    #Function to return list containing elements of right view of binary tree.
    def rightView(self,root):
        if (root == None):
            return []
        q = deque()
        q.append(root)
        q.append(None)
        ret = []
        t = []
        while (len(q) > 1):
            curr = q.popleft()
            if (curr == None):
                ret.append(t[-1])
                t = []
                q.append(None)
            else:
                if (curr.left):
                    q.append(curr.left)
                if (curr.right):
                    q.append(curr.right)
                t.append(curr.data)
        ret.append(t[-1])
        return ret