
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: Node) -> int:
        def help(root):
            if not root:
                return 0
            tp = []
            for i in root.children:
                tp.append(help(i))
            if len(tp)==0:
                return 1
            return max(tp) + 1
        
        return help(root)