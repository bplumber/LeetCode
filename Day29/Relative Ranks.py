class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        res = []
        while max(score)!=-1:
            cur = max(score)
            res.append([cur, score.index(cur)])
            score[score.index(cur)] = -1
        rank = []
        rank.append("Gold Medal")
        rank.append("Silver Medal")
        rank.append("Bronze Medal")
        x = 4
        if len(rank)<len(score):
            while len(rank)!=len(score):
                rank.append(str(x))
                x+=1
        for i in range(len(res)):
            res[i][0] = rank[i]
        for i in res:
            score[int(i[1])] = i[0]
        return score