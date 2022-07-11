class Solution:
    def maxArea(self, height: List[int]) -> int:
        # n = height.copy()
        # i = 0
        # j = len(n)-1
        # a = (len(n)-1)*min(n[i],n[j])
        # t1 = 0
        # t2 = 0
        # while i < j:
        #     if i+1 < j:
        #         t1 = (j - (i+1))*min(n[i+1],n[j])
        #     if i < j-1:
        #         t2 = ((j-1) - i)*min(n[i],n[j-1])
        #     if t1>t2:
        #         i+=1
        #         t = t1
        #     elif t1<t2:
        #         j-=1
        #         t = t2
        #     else:
        #         i+=1
        #         j-=1
        #         t = 0
        #     if a < t:
        #         a = t
        # return a
#         n = height.copy()
#         i = 0
#         j = len(n)-1
#         a = (len(n)-1)*min(n[i],n[j])
#         t1 = 0
#         t2 = 0
#         while i < j:
#             if i+1<j:
#                 if n[i]<n[i+1]:
#                     tp = (j-(i+1))*min(n[i+1], n[j])
#                     if a < tp:
#                         a = tp
#             i+=1
#             if i < j - 1:
#                 if n[j]<n[j-1]:
#                     tp = (j-1-i)*min(n[i], n[j-1])
#                     if a<tp:
#                         a = tp
#             j-=1
#         return a
        n = height.copy()
        i = 0
        j = len(n)-1
        a = (len(n)-1)*min(n[i],n[j])
        while i < j:
            ih = n[i]
            jh = n[j]
            a = max(a, (j-i)*min(ih, jh))
            if ih < jh:
                i+=1
            else:
                j-=1
        return a
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    