from math import sqrt
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        ct = 0
        for i in range(left, right+1):
            count = bin(i).count('1')
            if count!=1:
                isPrime = True
                for j in range(2, int(sqrt(count))+1):
                    if count%j==0:
                        isPrime = False
                if isPrime:
                    ct+=1
        return ct

# ALTERNATE SOLUTION
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        ct = 0
        for num in range(left, (right + 1)):
            if bin(num).count("1") in {2, 3, 5, 7, 11, 13, 17, 19}:
                ct += 1
        return ct

