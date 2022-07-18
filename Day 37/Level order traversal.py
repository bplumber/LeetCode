from collections import deque
class Solution:
    #Function to return the level order traversal of a tree.
    def levelOrder(self,root ):
        d = deque()
        d.append(root)
        rt = []
        while d:
            x = d.popleft()
            rt.append(x.data)
            if x.left:
                d.append(x.left)
            if x.right:
                d.append(x.right)
        return rt