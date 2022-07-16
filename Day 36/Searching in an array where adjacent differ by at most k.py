def search (arr, n, x, k) : 
    for i in range(len(arr)):
        if arr[i]==x:
            return i
    return -1
