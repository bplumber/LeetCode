class Solution:
    #Function to convert a binary tree into its mirror tree.
    def mirror(self,root):
        if not root:
            return None
        root.right, root.left = root.left, root.right
        self.mirror(root.left)
        self.mirror(root.right)
        return root