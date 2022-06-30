class Solution:
    def numUniqueEmails(self, emails) -> int:
        rt = set()
        for i in emails:
            x = i.split('@')
            t = x[0].index('+') if '+' in x[0] else None
            if t is not None:
                x[0] = x[0][:t]
            x[0] = x[0].replace('.', '')
            rt.add(str(x[0])+'@'+x[1])
        return len(rt)