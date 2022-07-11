def minValue(root):
    def hlp(root):
        if not root:
            return -1
        if root.left is None:
            return root.data
        else:
            return hlp(root.left)
    
    return hlp(root)