def find(arr,n,x):
    st = -1
    en = -1
    for i in range(n):
        if arr[i]==x:
            st = i
            for j in range(st, n):
                if arr[j]==x:
                    en = j
                else:
                    break
            break
    return st, en