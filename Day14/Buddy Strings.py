from collections import Counter
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        diff = 0
        diff_lt = []
        if len(s)!=len(goal):
            return False
        for i in range(len(s)):
            if s[i]!=goal[i]:
                diff_lt.append(i)
                diff+=1
                if diff>2:
                    return False
        if diff == 2 and (s[diff_lt[0]] == goal[diff_lt[1]] and s[diff_lt[1]] == goal[diff_lt[0]]):
            return True
        if diff == 0:
            s_dick = dict(Counter(s))
            goal_dick = dict(Counter(goal))
            if (max(s_dick.values())>1 and max(goal_dick.values())>1) and (list(s_dick.keys())[list(s_dick.values()).index(max(s_dick.values()))]==list(goal_dick.keys())[list(goal_dick.values()).index(max(goal_dick.values()))]):
                return True