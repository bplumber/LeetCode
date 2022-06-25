# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        arr = []
        def hasPath(root, x, arr):
            if (not root):
                return False
            arr.append(root.val)    
            if (root.val == x.val):    
                return True
            if (hasPath(root.left, x, arr) or hasPath(root.right, x, arr)):
                return True
            arr.pop()
            return False
        arr = []
        hasPath(root, p, arr)
        pp = arr.copy()
        arr = []
        hasPath(root, q, arr)
        qp = arr.copy()
        print(pp, qp)
        i = 0
        while pp != qp:
            if len(pp)==len(qp):
                pp.pop()
                qp.pop()
            elif len(pp)>len(qp):
                pp.pop()
            elif len(pp)<len(qp):
                qp.pop()
        
        return TreeNode(pp[-1])


#ACTUAL ANSWER

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         The trick in this question was utilising the fact that it was binary SEARCH tree
#         Because of this we knew that if 2 numbers ever split off - then their last common ancestor would be the node that the split off on
#         Otherwise you'd have to check further
#         The only time they WOULD split off is if:
#             -> P < Root < Q
#             -> or P > root > Q
#         -> So just keep recursivley doing the traversal untill that condition is met 
        
        
        if p.val > root.val and q.val > root.val:
            return(self.lowestCommonAncestor(root.right, p, q))
        
        elif p.val < root.val and q.val < root.val:
            return(self.lowestCommonAncestor(root.left, p, q))
        return root