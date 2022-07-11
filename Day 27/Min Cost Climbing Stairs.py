class Solution:
    def minCostClimbingStairs(self, cost: int) -> int:
        cost = cost[::-1]
        f = []
        f.append(cost[0])
        f.append(cost[1])
        for i in range(2, len(cost)):
            f.append(min(f[i-1], f[i-2])+cost[i])
        return min(f[-1],f[-2])