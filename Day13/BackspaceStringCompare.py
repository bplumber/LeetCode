class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stackOne, stackTwo = [], []
        
        for i in s:
            if i == '#':
                if stackOne:
                    stackOne.pop()
                    
            else:
                stackOne.append(i)
                
        for i in t:
            if i == '#':
                if stackTwo:
                    stackTwo.pop()
            else:
                stackTwo.append(i)
                
                
        return stackOne == stackTwo 