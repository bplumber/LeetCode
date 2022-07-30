class Solution:
    def inOrder(self, root):
        d = []
        cur = root
        lt = []
        while cur or d:
            if cur:
                d.append(cur)
                cur = cur.left
            else:
                cur = d.pop()
                lt.append(cur.data)
                cur = cur.right
        return lt