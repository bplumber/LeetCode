class Solution:
    def maxSubStr(self,str):
        #Write your code here
        chk = 0
        stk = []
        ct = 0
        for i in str:
            i = int(i)
            if chk == 0:
                if i == 0:
                    stk.append(i)
                elif i == 1 and len(stk)!=0:
                    stk.pop()
                    if len(stk)==0:
                        ct+=1
                elif i == 1 and len(stk)==0:
                    chk = 1
                    stk.append(i)
            else:
                if i == 1:
                    stk.append(i)
                elif i == 0 and len(stk)!=0:
                    stk.pop()
                    if len(stk)==0:
                        ct+=1
                elif i == 0 and len(stk)==0:
                    chk = 0
                    stk.append(i)
        if len(stk)==0:
            return ct   
        else:
            return -1