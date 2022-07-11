# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        rt = 0
        def help(root):
            nonlocal rt
            if not root:
                return 
            help(root.left)
            help(root.right)
            if root.left and root.right:
                root.val +=(root.left.val+root.right.val)
                rt+=abs(root.left.val-root.right.val)
            elif root.left:
                root.val += root.left.val
                rt+=abs(root.left.val)
            elif root.right:
                root.val += root.right.val
                rt+=abs(root.right.val)
        help(root)
        return rt