def start():
    mat = [[1,2,3],
                [4,5,6],
                [7,8,9]]
    n = len(mat)
    m = len(mat[0])
    i = 0
    def hlp(path,n,m,pi):
        nonlocal i
        path[pi] = mat[n][m]
        if n == 0 and m == 0:
            print(path)
            return 0
        if n == 0:
            hlp(path, n, m-1, pi-1)
            return 1
        if m == 0:
            hlp(path, n-1, m, pi-1)
            return 1
        
        return hlp(path, n, m-1, pi-1) + hlp(path, n-1, m, pi-1)

    path = []
    for i in range(n+m-1):
        path.append(-1)
    hlp(path, n-1, m-1, len(path)-1)

start()