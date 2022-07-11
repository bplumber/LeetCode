class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        lt = []
        for i in range(len(strs[0])):
            lt.append([])
        for i in range(len(strs)):
            for j in range(len(strs[i])):
                lt[j].append(strs[i][j])
        ct = 0
        for i in lt:
            j = i[:]
            j.sort()
            if i!=j:
                ct+=1
        return ct