from collections import OrderedDict
class Solution:
    def firstNonRepeating(self, arr, n): 
        # dick = OrderedDict()
        # for i in arr:
        #     if i in dick:
        #         dick[i]+=1
        #     else:
        #         dick[i]=1
        # for k, v in dick.items():
        #     if v==1:
        #         return k
        # return 0
        dick = {}
        x = 0
        for i in arr:
            if i not in dick:
                tp = [x, 1, i]
                dick[i] = tp
                x+=1
            else:
                tp = dick[i]
                tp[1] = tp[1]+1
                dick[i] = tp
        temp = []
        for i in dick.values():
            if i[1]==1:
                temp.append(i)
        if len(temp)==0:
            return 0
        else:
            temp.sort()
            return temp[0][2]