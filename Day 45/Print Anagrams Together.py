class Solution:
    def Anagrams(self, words, n):
        dick = {}
        for i in words:
            j = ''.join(sorted(i))
            if j in dick:
                dick[j].append(i)
            else:
                dick[j] = [i]
        tp = []
        for i in words:
            j = ''.join(sorted(i))
            if j in dick:
                tp.append(dick[j])
                del dick[j]
        return tp