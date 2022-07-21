class Solution:
    def findDuplicateSubtrees(self, root):
        dick = {}
        lt = []
        def hlp(root):
            nonlocal dick, lt
            if not root:
                return '$'
            l=hlp(root.left)
            r=hlp(root.right)
            s = l + "," + r + "," + str(root.val)
            if s in dick:
                dick[s]+=1
                if dick[s]==2:
                    lt.append(root)
            else:
                dick[s]=1
            return s
        
        hlp(root)
        return lt