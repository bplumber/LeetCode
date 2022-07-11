class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)==len(goal):
            n = len(s)
            check = [0]*n
            for _ in range(n+1):
                for i in range(1,n+2):
                    check[(i+1)%n] = s[i%n]
                if ''.join(check) == goal:
                    return True
                s = ''.join(check)
