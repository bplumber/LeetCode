import sys
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root):
        mn = sys.maxsize
        prev = None
        def help(root):
            nonlocal mn, prev
            if not root:
                return
            help(root.left)
            if prev is not None:
                if abs(prev - root.val)<mn:
                    mn = abs(prev - root.val)
            prev = root.val
            help(root.right)
        help(root)
        return mn