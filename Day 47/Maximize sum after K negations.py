class Solution:
    def maximizeSum(self, a, n, k):
        a.sort()
        for i in range(len(a)):
            if a[i]>=0 or k==0:
                break
            a[i] = a[i]+((-2)*(a[i]))
            k-=1
        if k%2!=0:
            a.sort()
            a[0]=a[0]-(2*a[0])
        return sum(a)