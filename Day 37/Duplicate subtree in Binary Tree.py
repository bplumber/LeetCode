class Solution:
    def dupSub(self, root):
        dick = {}
        
        def hlp(root):
            nonlocal dick
            if not root:
                return '$'
            s = ""
            if not root.left and not root.right:
                return str(root.data)
            s+=str(root.data)
            s+=hlp(root.left)
            s+=hlp(root.right)
            if s in dick:
                dick[s]+=1
            else:
                dick[s]=1
            return s
        
        hlp(root)
        if len(dick)==0:
            return 0
        if max(dick.values())>=2:
            return 1
        return 0