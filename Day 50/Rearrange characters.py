class Solution :
    def rearrangeString(self, str):
        n = len(str)
        lt = [0]*26
        a = ord('a')
        for i in str:
            lt[ord(i)-a]+=1
        mxcount = 0
        for i in range((len(lt))):
            if lt[i] > mxcount:
                mxcount = lt[i]
                mxchar = chr(a+i)
        if mxcount > (n+1)/2:
            return '-1'
        res = [0]*n
        ind = 0
        while mxcount:
            res[ind] = mxchar
            ind+=2
            mxcount-=1
        lt[ord(mxchar)-a] = 0
        for i in range(26):
            while lt[i]>0:
                if ind>=n:
                    ind = 1
                res[ind] = chr(i+a)
                lt[i]-=1
                ind+=2
        rs=''
        for i in res:
            rs+=i
        return rs
        