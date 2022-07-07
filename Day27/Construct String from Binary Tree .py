# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def tree2str(self, root: TreeNode) -> str:
        def hlp(root):
            if not root:
                return ""
            if not root.left and not root.right:
                return str(root.val)
            lt = hlp(root.left)
            rt = hlp(root.right) 
            if rt =="":
                return str(root.val) + "(" + lt +")"
            else:
                return str(root.val) + "(" + lt +")" + "(" + rt +")"
        return hlp(root)