# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root)
        main = []
        def leaf_help(root, leaf):
            if not root:
                return
            if not leaf:
                leaf = str(root.val)
            else:
                leaf = leaf + "->" + str(root.val)
            if root.left is None and root.right is None:
                main.append(leaf)
                return
            leaf_help(root.left, leaf)
            leaf_help(root.right, leaf)
        leaf_help(root, "")
        return main
        