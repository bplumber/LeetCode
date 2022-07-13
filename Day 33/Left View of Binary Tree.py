from collections import deque
def LeftView(root):
    rt = []
    def hlp(root, level):
        nonlocal rt
        if root is None:
            return 
        if level == len(rt):
            rt.append(root.data)
        hlp(root.left, level+1)
        hlp(root.right, level+1)
    
    hlp(root, 0)
    return rt