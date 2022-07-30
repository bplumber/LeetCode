class Solution:
    # Return a list containing the inorder traversal of the given tree
    def preOrder(self, root):
        d = []
        lt = []
        d.append(root)
        while d:
            x = d.pop()
            lt.append(x.data)
            if x.right:
                d.append(x.right)
            if x.left:
                d.append(x.left)

                
        return lt