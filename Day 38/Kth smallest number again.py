t = int(input())
for i in range(t):
    n, q = list(map(int,input().split()))
    rnge = []
    for i in range(n):
        a, b = list(map(int,input().split()))
        rnge.append([a,b])
    rnge.sort()
    idx = 0
    for i in range(1,len(rnge)):
        if rnge[idx][1]>=rnge[i][0]:
            rnge[idx][1] = max(rnge[idx][1],rnge[i][1])
        else:
            idx+=1
            rnge[idx] = rnge[i]
    for i in range(q): 
        k = int(input())
        ans = -1
        for x in range(idx+1):
            if k <= (rnge[x][1]-rnge[x][0]+1):
                ans = rnge[x][0]+k-1
                break
            else:
                k = k - (rnge[x][1]-rnge[x][0]+1)
        print(ans)