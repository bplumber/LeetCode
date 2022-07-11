# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        rt = 0
        def ass(root, x):
            nonlocal rt
            if not root:
                return
            if root.left is None and root.right is None:
                if x == 'l':
                    rt+=root.val
            ass(root.left, 'l')
            ass(root.right, 'r')
        
        ass(root, 'r')
        return rt