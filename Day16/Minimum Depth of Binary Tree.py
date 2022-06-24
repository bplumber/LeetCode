from collections import deque

 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        def help(root, temp):
            if root is None:
                return 0, temp
            lt, temp = help(root.left, temp)
            rt, temp = help(root.right, temp)
            temp = [lt + 1, rt + 1]
            if lt == 0 or rt == 0:
                return max(lt, rt)+1, temp
            else:
                return min(lt, rt)+1, temp
        tp, temp = help(root, [])
        if min(temp[0], temp[1]) ==1:
            return max(temp[0], temp[1])
        return min(temp[0], temp[1])
       

# ALTERNATE SOLUTION

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque()
        q.append(root)
        
        curr_depth = 0
        while q:
            level_size = len(q)
            curr_depth += 1
            
            for _ in range(level_size):
                curr = q.popleft()
                if curr:
                    if not curr.right and not curr.left:
                        return curr_depth
                    
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
        
        return 0