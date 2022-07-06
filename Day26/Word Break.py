def wordBreak(line, dictionary):
    dick = {}
    def dfs(s):
        nonlocal dick
        if s == "":
            return True
        if s in dick:
            return dick[s]
        for i in range(1, len(s)+1):
            if s[0:i] in dictionary and dfs(s[i:len(s)]):
                dick[s[i:len(s)]] = True
                return True
        dick[s] = False
        return False    
        
    return dfs(line)