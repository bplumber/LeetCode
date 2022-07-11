n =7
s = bin(n)[2:]
for i in range(len(s)-1):
    if s[i]=='0' and s[i+1]!='1':
        print(False)
    if s[i]=='1' and s[i+1]!='0':
        print(False)
print(True)