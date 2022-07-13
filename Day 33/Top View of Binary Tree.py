class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        dick = {}
        d = deque()
        d.append([root, 0])
        while d:
            x = d.popleft()
            if x[1] not in dick:
                dick[x[1]] = x[0].data
            if x[0].left:
                d.append([x[0].left, x[1]-1])
            if x[0].right:
                d.append([x[0].right, x[1]+1])
            
        ret = []
        for i in sorted(dick.keys()):
            ret.append(dick[i])
        
        return ret