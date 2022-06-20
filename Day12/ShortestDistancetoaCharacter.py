class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        s = s.replace(c, '0')
        ind = []
        for i in range(len(s)):
            if s[i] == '0':
                ind.append(i)
        main = []
        if s[0]!='0':
            for i in range(ind[0], 0, -1):
                main.append(i)
        main.append(0)
        for i in range(0,len(ind)-1):
            dif = abs(ind[i]-ind[i+1])-1
            temp = []
            for j in range(1,int(dif/2)+1):
                temp.append(j)
            for x in temp:
                main.append(x)
            if dif%2!=0:
                main.append(main[-1]+1)  
            temp = temp[::-1]
            for x in temp:
                main.append(x)
            temp = []
            main.append(0)
        if ind[-1]!=len(s)-1:
            i = 1
            while len(main)!=len(s):
                main.append(i)
                i+=1
        return main