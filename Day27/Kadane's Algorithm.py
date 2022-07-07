class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        if max(arr)<=0:
            return max(arr)
        for j in range(N):
            if arr[j]>0:
                break
        mx = arr[j]
        mxl = []
        mxl = mx
        for i in range(j+1, N):
            if arr[i]<0 and mx+arr[i]>0:
                mxl = max(mxl, mx)
                mx+=arr[i]
            elif arr[i] < 0 and mx+arr[i] <= 0:
                mxl = max(mxl, mx)
                mx=0
            else:
                mx+=arr[i]
        mxl = max(mxl, mx)
        
        return mxl