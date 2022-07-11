def reverse(S):
    x = []
    for i in S:
        x.append(i)
    rt = ""
    while len(x)!=0:
        rt+=x.pop()
    return rt