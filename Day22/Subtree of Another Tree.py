# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot:TreeNode) -> bool:
        def chk(r1, r2):
            if not r1 and not r2:
                return True
            if not r1 or not r2 or r1.val != r2.val:
                return False
            return chk(r1.left, r2.left) and chk(r1.right, r2.right)
        
        q = deque()
        q.append(root)
        while len(q) > 0:
            temp = q.popleft()
            if temp.val == subRoot.val:
                if chk(temp, subRoot):
                    return True
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        return False