# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True
        def help(root, isBalanced):
            if root is None:
                return 0, isBalanced
            lt, isBalanced = help(root.left, isBalanced)
            rt, isBalanced = help(root.right, isBalanced)
            if abs(lt-rt)>1:
                isBalanced = False
            return max(lt, rt) +1, isBalanced
        mx, isBalanced = help(root, isBalanced)
        return isBalanced