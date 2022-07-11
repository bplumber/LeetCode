class Solution:
    
    #Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        mn = -999999999999999
        mx = 9999999999999999    
        def helper(root, mn, mx):
            if root is None:
                return True
            if root.data > mn and root.data<mx:
                return helper(root.left, mn, root.data) and helper(root.right, root.data, mx)
            return False
        return helper(root, mn, mx)