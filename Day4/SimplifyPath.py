path = "/home//foo/"
check=[]
check[:0]=path
check = list(set(check))
if check[0] =='/':
    print('/')
while path[-1]=='/':
    path = path[:-1]
while "//" in path:
    path = path.replace("//", "/")
lt = path.split("/")
ret = []
for i in lt:
    try:
        if i=="..":
            ret.pop()
        elif i!='.':
            ret.append(i)
    except:
        continue
if len(ret)==0:
    print('/')
if ret[0]=='':
    ret = ret[1:]
print('/'+'/'.join(ret))