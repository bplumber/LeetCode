class Solution:
    def restoreString(self, s: str, indices) -> str:
        n = ['']*len(s)
        for i,j in zip(s, indices):
            n[j] = i
        return ''.join(n)