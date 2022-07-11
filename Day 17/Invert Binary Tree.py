# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return 
        def help(tp):
            if tp is None:
                return
            if tp.left and tp.right:
                tp.left,tp.right = tp.right,tp.left
            elif tp.left:
                tp.right = tp.left
                tp.left = None
            elif tp.right:
                tp.left = tp.right
                tp.right = None
            help(tp.left)
            help(tp.right)
         
        help(root)
        return root
        
# ALTERNATE SOLUTION

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return 
        def help(tp):
            if tp is None:
                return
            tp.left,tp.right = tp.right,tp.left
            help(tp.left)
            help(tp.right)
         
        help(root)
        return root