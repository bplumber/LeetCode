# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def lr(l,r):
            if r<l:
                return None
            else:
                mid = (l+r)//2
                root = TreeNode(nums[mid])
                root.left = lr(l, mid-1)
                root.right = lr(mid+1, r)
                return root
        return lr(0,len(nums)-1)