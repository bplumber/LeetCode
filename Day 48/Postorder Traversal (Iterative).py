class Solution:
    # Return a list containing the inorder traversal of the given tree
    def postOrder(self,root):
        d = []
        o = []
        d.append(root)
        while d:
            x = d.pop()
            o.append(x.data)
            if x.left:
                d.append(x.left)
            if x.right:
                d.append(x.right)
        
        return o[::-1]