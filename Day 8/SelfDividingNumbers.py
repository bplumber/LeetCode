class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        main = []
        for n in range(left,right+1):
            tp = []
            for i in str(n):
                tp.append(i)
            tp_set = set(tp)
            try:
                tp_set.remove('0')
            except:
                pass
            ct = 0
            for i in tp_set:
                if n%int(i)==0:
                    ct+=1
            if ct == len(tp_set) and '0' not in tp:
                main.append(n)
        return main
            
# ALTERNATE SOLUTION

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        record = []
        for i in range(left, right+1):
            if '0' in str(i):
                continue
            else:
                append = True
                for digit in str(i):
                    if i%int(digit)!=0:
                        append = False
                        break
                if append:
                    record.append(i)
        
        return record