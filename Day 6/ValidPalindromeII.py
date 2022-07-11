from collections import Counter
s = "abca"
if (len(s))%2==0:
    if s[:int(len(s)/2)] == s[int(len(s)/2):][::-1]:
        print(True)
else:
    if s[:int(len(s)/2)] == s[int(len(s)/2)+1:][::-1]:
        print(True)
dick = dict(Counter(s))
odd = []
for key, val in dick.items():
    if val%2!=0:
        odd.append(key)
if (len(s)-1)%2==0:
    for i in odd:
        t = s.replace(i,"")
        if t[:int(len(t)/2)] == t[int(len(t)/2):][::-1]:
            print(True)
else:
    for i in odd:
        t = s.replace(i,"")
        if t[:int(len(t)/2)] == t[int(len(t)/2)+1:][::-1]:
            print(True)