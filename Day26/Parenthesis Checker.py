class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        stk = []
        for i in x:
            if i == '(' or i == '[' or i == '{':
                stk.append(i)
            if (i == ']' or i == ')' or i == '}') and len(stk)==0:
                return False
            # if len(stk)>0:
            if i == ')' and stk[-1]=='(':
                if stk[-1] == '(':
                    stk.pop()
                else:
                    return False
            elif i == ']':
                if stk[-1] == '[':
                    stk.pop()
                else:
                    return False
            elif i == '}':
                if stk[-1] == '{':
                    stk.pop()
                else:
                    return False
        return len(stk)==0