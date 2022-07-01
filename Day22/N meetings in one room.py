class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        x = []
        ct = 1
        for i, j in zip(start, end):
            x.append([i,j])
        x.sort(key = lambda i:i[1])
        en = x[0][1]
        for i in range(1,len(x)):
            if en < x[i][0]:
                en = x[i][1]
                ct+=1
        return ct