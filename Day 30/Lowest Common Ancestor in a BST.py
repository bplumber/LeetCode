def LCA(root, n1, n2):
   #code here.
   if (n1 >= root.data and n2 <= root.data) or (n1 <= root.data and n2 >= root.data):
       return root
   elif n1 >= root.data and n2 >= root.data:
       return LCA(root.right, n1, n2)
   else:
       return LCA(root.left, n1, n2)