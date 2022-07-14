class Solution:
    
    #Function to evaluate a postfix expression.
    def evaluatePostfix(self, S):
        op = {'+': lambda x, y: x + y,
              '-': lambda x, y: x - y,
              '*': lambda x, y: x * y,
              '/': lambda x, y: x / y
        }
        stk = []
        for i in S:
            if i.isnumeric():
                stk.append(i)
            else:
                y = stk.pop()
                x = stk.pop()
                res = int(op[i](int(x),int(y)))
                stk.append(res)
            # print(stk)
        return int(stk[0])