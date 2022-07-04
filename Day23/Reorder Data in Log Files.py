class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        l = []
        d = []
        for i in range(len(logs)):
            logs[i] = logs[i].split(" ")
            if logs[i][1].isalpha():
                l.append([' '.join(logs[i][1:]), logs[i][0]])
            else:
                d.append(' '.join(logs[i]))
        l.sort()
        for i in range(len(l)):
            l[i] = l[i][::-1]
            l[i] = ' '.join(l[i])
        return l + d