from collections import deque
def LeftView(root):
    if (root == None):
        return []
    q = deque()
    q.append(root)
    q.append(None)
    ret = []
    t = []
    while (len(q) > 1):
        curr = q.popleft()
        if (curr == None):
            ret.append(t[0])
            t = []
            q.append(None)
        else:
            if (curr.left):
                q.append(curr.left)
            if (curr.right):
                q.append(curr.right)
            t.append(curr.data)
    ret.append(t[0])
    return ret