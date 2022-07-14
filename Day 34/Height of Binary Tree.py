class Solution:
    #Function to find the height of a binary tree.
    def height(self, root):
        def hlp(root):
            if not root:
                return 0
            return max(hlp(root.left), hlp(root.right))+1
        return hlp(root)