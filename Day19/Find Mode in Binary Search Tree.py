# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findMode(self, root: TreeNode):
        dick = {}
        def help(root):
            nonlocal dick
            if not root:
                return
            if root.val in dick:
                dick[root.val]+=1
            else:
                dick[root.val] = 1
            help(root.left)
            help(root.right)
        help(root)
        mx = max(dick.values())
        rt = []
        for i, v in dick.items():
            if v == mx:
                rt.append(i)
        return rt