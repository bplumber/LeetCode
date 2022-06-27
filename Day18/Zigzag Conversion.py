class Solution:
    def convert(self, s: str, numRows: int) -> str:
        temp = []
        main = []
        chk = 0
        x = 0
        for i in s:
            if chk==0:
                temp.append(i)
                if len(temp)==numRows:
                    main.append(temp)
                    temp = []
                    chk = max(numRows - 2, 0)
            elif chk != 0:
                while x!=chk:
                    temp.append(" ")
                    x+=1
                temp.append(i)
                x = 0
                while len(temp) != numRows:
                    temp.append(" ")
                main.append(temp)
                temp = []
                chk-=1
        if len(temp)!=0:
            main.append(temp)
        rt = []
        for i in range(numRows):
            rt.append("")
        for i in range(len(main)):
            for j in range(len(main[i])):
                rt[j]+=main[i][j]
        rt = ''.join(rt)
        rt = rt.replace(" ", "")
        return  rt