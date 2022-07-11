class Solution:
    def findTwoElement( self,arr, n): 
        rep, miss = 0, []
        arr.sort()
        for i in range(len(arr)-1):
            if arr[i]==arr[i+1]:
                rep = arr[i]
        arrsum  = (n*(n+1))/2
        setsum  = sum(set(arr))
        
        return rep, int(arrsum - setsum)
