ops = ["5","-2","4","C","D","9","+","+"]
lt = []
for i in ops:
    if i == '+':
        lt.append(lt[-1]+lt[-2])
    elif i == 'D':
        lt.append(2*lt[-1])
    elif i == 'C':
        lt.pop()
    else:
        lt.append(int(i))
print(sum(lt))