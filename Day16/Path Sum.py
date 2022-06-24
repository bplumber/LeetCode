import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        q = collections.deque()
        q.append(root)
        while q:
            lvl = len(q)
            for _ in range(lvl):
                curr = q.popleft()
                if curr.left is None and curr.right is None:
                    if curr.val == targetSum:
                        return True
                if curr.left:
                    curr.left.val = curr.left.val + curr.val
                    q.append(curr.left)
                if curr.right:
                    curr.right.val = curr.right.val + curr.val
                    q.append(curr.right)
        return False
    
#ALTERNATE SOLUTION

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        targetSum -= root.val
        if not root.left and not root.right: 
            return targetSum == 0
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)