class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        dick = {}
        dick['2'] = ['a','b','c']
        dick['3'] = ['d','e','f']
        dick['4'] = ['g','h','i']
        dick['5'] = ['j','k','l']
        dick['6'] = ['m','n','o']
        dick['7'] = ['p','q','r','s']
        dick['8'] = ['t','u','v']
        dick['9'] = ['w','x','y','z']
        main = []
        ln = 1
        mult = []
        for i in digits:
            mult.append(len(dick[i]))
            ln = ln*len(dick[i])
        for i in range(ln):
            main.append("")
        z = 0
        for i in digits:
            ln = ln/mult[z]
            x = 0
            chk = 0
            for j in range(len(main)):
                main[j] = main[j] + dick[i][x]
                chk+=1
                if chk==ln:
                    x+=1
                    if x >= len(dick[i]):
                        x = 0
                    chk=0
            z+=1
        return main