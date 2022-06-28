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

# ALTERNATE SOLUTION

class Solution:
    def findMode(self, root:TreeNode) :
        lt = []
        count = 1
        mx = 0
        prev = None
        def help(root):
            nonlocal count
            nonlocal mx
            nonlocal prev
            if not root:
                return
            help(root.left)
            if prev is not None:
                if prev == root.val:
                    count+=1
                else:
                    count = 1
            if count>mx:
                mx = count
                lt.clear()
                lt.append(root.val)
            elif count == mx:
                lt.append(root.val)
            prev = root.val
            help(root.right)
        help(root)
        return lt