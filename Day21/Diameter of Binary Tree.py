# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        mx = 0
        def help(root):
            nonlocal mx
            if not root:
                return 0
            lt = help(root.left)
            rt = help(root.right)
            if mx < lt+rt:
                mx = lt+rt
            return max(lt, rt) + 1
        help(root)
        return mx