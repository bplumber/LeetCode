n = int(input())
for _ in range(n):
    lt = list(map(int, input().split()))
    r = [-1]
    c = [-1]
    for _ in range(lt[2]):
        tp = list(map(int, input().split()))
        c.append(tp[0]-1)
        r.append(tp[1]-1)
    r.append(lt[1])
    c.append(lt[0])
    r.sort()
    c.sort()  
    print(r,c)
    cn = len(c) 
    rn = len(r)
    mxl, mxb = 0, 0
    i, j = 0, 1
    while j < cn:
        l = c[j]-c[i]-1
        if l > mxl:
            mxl = l
        i+=1
        j+=1
    x, y = 0, 1
    while y < rn:
        b = r[y]-r[x]-1
        if b>mxb:
            mxb = b
        x+=1
        y+=1
    print(mxl*mxb)

