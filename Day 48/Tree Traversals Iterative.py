# Data structure to store a binary tree node
class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def pre(root):
    d = []
    d.append(root)
    while d:
        x = d.pop()
        print(x.data, end=" ")
        if x.left:
            d.append(x.left)
        if x.right:
            d.append(x.right)

def pos(root):
    d = []
    o = []
    d.append(root)
    while d:
        x = d.pop()
        o.append(x.data)
        if x.left:
            d.append(x.left)
        if x.right:
            d.append(x.right)
    while o:
        x = o.pop()
        print(x, end = " ")

def ino(root):
    d = []
    cur = root
    while cur or d:
        if cur:
            d.append(cur)
            cur = cur.left
        else:
            cur = d.pop()
            print(cur.data, end = " ")
            cur = cur.right
   
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
     
    ino(root)
    print()
    pos(root)
    print()
    pre(root)