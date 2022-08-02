def maxSum(arr,n):
    arr.sort()
    i = 0
    j = n-1
    sm = 0
    nt = True
    while i < j:
        sm += abs(arr[i]-arr[j])
        if not nt:
            j-=1
        else:
            i+=1
        nt = not nt
    sm += abs(arr[i]-arr[0])
    return sm