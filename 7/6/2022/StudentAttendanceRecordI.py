s = "PPLPPLLPLPPPPPPPPPPLPLPPLPLPPP"
A = 0
L = []
for i in range(len(s)):
    if s[i] == 'A':
        A += 1
    elif s[i] == 'L':
        L.append(i)
tp = []
for i in range(len(L)-1):
    if L[i+1]-L[i]>10:
        tp.append('x')
    else:
        tp.append(str(L[i+1]-L[i]))
if '11' not in ''.join(tp) and A<2:
    print("True")
else:
    print('False')