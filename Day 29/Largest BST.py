class Solution:
    # Return the size of the largest sub-tree which is also a BST
    def largestBst(self, root):
        INT_MAX=[999999]
        INT_MIN=[-999999]
        def postorder(root):
            
            if not root:
                return [1, 0, INT_MAX[0] , INT_MIN[0]]
                
            if not root.left and not root.right:
                return [1, 1, root.data, root.data]
            
            l=postorder(root.left)
            r=postorder(root.right)
            if l[0] and r[0]:
                if root.data>l[3] and root.data<r[2]:
                    x=l[2]
                    y=r[3]
                    if x==INT_MAX[0]:
                        x=root.data
                    if y==INT_MIN[0]:
                        y=root.data
                    return [1, l[1]+r[1]+1 ,x ,y ]
            return [0, max(l[1],r[1]), 0 , 0]
            
        arr=postorder(root)
        return arr[1]
