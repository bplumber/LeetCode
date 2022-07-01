class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        j = []
        time = 0
        for i in Jobs:
            j.append([i.id, i.deadline, i.profit])
            if i.deadline > time:
                time = i.deadline
        j.sort(key = lambda i:i[2], reverse = True)
        jobs = [0]*time
        t = 1
        c = 0
        pro = 0
        for i in j:
            if 0 in jobs[:i[1]]:
                a = i[1]-1
                while(jobs[a]!=0 and a>=0):
                    a-=1
                if a >= 0:
                    jobs[a]=1
                    c+=1
                    pro+=i[2]
                    t+=1
        return c, pro