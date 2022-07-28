class Solution:
    def buyMaximumProducts(self, n : int, k : int, price : List[int]) -> int:
        stk = 0
        n = []
        for i in range(len(price)):
            n.append([price[i], i+1])
        n.sort()
        for i in n:
            x = i[1]
            while x!=0 and i[0]<=k:
                x-=1
                k-=i[0]
                if k >= 0:
                    stk+=1
        return stk