from collections import deque
class Solution:
    def bottomView(self, root):
        dick = {}
        d = deque()
        d.append([root, 0])
        while d:
            x = d.popleft()
            dick[x[1]] = x[0].data
            if x[0].left:
                d.append([x[0].left, x[1]-1])
            if x[0].right:
                d.append([x[0].right, x[1]+1])
        lt = []
        for i in sorted(dick.keys()):
            lt.append(dick[i])
        return lt