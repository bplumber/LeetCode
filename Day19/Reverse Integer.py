class Solution:
    def reverse(self, x: int) -> int:
        mx = 2147483647
        if x == 0:
            return 0
        lt = ""
        neg = 0
        if x < 0:
            neg = 1 
            x = abs(x)
        while x > 0:
            digit = int(x%10)
            x=int(x/10)
            if len(lt)!=0:
                if int(lt)>mx//10 or (int(lt)==mx and digit >= int(mx%10)):
                    return 0
            lt+=str(digit)
        if neg==1:
            lt = '-'+lt
        return int(lt)
