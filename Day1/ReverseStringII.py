s = "abcdefg" 
k = 2
st = ""
lt = []
for i in s:
  st+=i
  if len(st) == 2*k:
    lt.append(st)
    st=""
lt.append(st)
st = ""
for i in lt:
  st += i[:k][::-1]+i[k:]
print(st)
