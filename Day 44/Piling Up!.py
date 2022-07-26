k = int(input())
for i in range(k):
    x = int(input())
    n = list(map(int, input().split()))
    i = 0
    j = x-1
    stk = max(n)
    fls = 0
    while i!=j:
        if n[i]>n[j] and n[i]<=stk:
            stk = n[i]
            i+=1
        elif n[j]>=n[i] and n[j]<=stk:
            stk = n[j]
            j-=1
        else:
            fls = 1
            break
    if fls:
        print("No")
    else:
        print("Yes")