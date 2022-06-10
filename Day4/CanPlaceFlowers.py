flowerbed = [1,0,0,0,1]
n = 1
tp = []
temp = []
for i in flowerbed:
    if i == 1:
        tp.append(temp)
        temp = []
    if i == 0:
        temp.append(0)
tp.append(temp)
if flowerbed[-1]==1:
    tp.append([])
possible = 0
for i in range(1,len(tp)-1):
    if len(tp[i])>=3 and len(tp[i])%2!=0:
        possible+=int(len(tp[i])/2)
    if len(tp[i])>=3 and len(tp[i])%2==0:
        possible+=int(len(tp[i])/2)-1
if len(tp[0])>=2 and flowerbed[0]==0 and len(tp)!=1:
    possible+=int(len(tp[0])/2)
if len(tp[0])>=2 and flowerbed[0]==0 and len(tp)==1:
    possible+=int(math.ceil(len(tp[0])/2))
if len(tp[-1])>=2 and flowerbed[-1]==0 and len(tp)>1:
    possible+=int(len(tp[-1])/2)
if len(flowerbed)==1 and flowerbed[0]==0:
    possible+=1
if possible>=n:
    print(True)
else:
    print(False)