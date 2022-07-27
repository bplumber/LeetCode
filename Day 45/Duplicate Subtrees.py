
class Solution:
    def printAllDups(self,root):
        d = {}
        lt = []
        def dfs(root):
            nonlocal d, lt
            if not root:
                return '$'
            l = dfs(root.left)
            r = dfs(root.right)
            s = l + ',' + r + ',' + str(root.data)
            if s in d:
                d[s]+=1
                if d[s]==2:
                    lt.append(root)
            else:
                d[s]=1
            return s
        
        dfs(root)
        return lt