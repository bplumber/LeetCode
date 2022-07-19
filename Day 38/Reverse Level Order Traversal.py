from collections import deque
def reverseLevelOrder(root):
    lt = []
    d = deque()
    d.append([root])
    main = [[root.data]]
    while d:
        i = d.popleft()
        temp = []
        tp1 = []
        for x in i: 
            lt.append(x.data)
            if x.left:
                temp.append(x.left)
                tp1.append(x.left.data)
            if x.right:
                temp.append(x.right)
                tp1.append(x.right.data)
        if len(temp)!=0:
            main.append(tp1)
            d.append(temp)
    main = main[::-1]
    return sum(main, [])