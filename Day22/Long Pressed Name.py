class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(name)==1 or len(typed)==1:
            if name == typed:
                return True
            if len(typed)==1 and len(name)!=1:
                return False
            if len(typed)!=1 and len(name)==1:
                if name[0] == list(set(typed))[0]:
                    return True
            else:
                return False
        nm = []
        i = 0
        j = 0
        while j < len(name)-1:
            j = i+1
            while name[j]==name[i] and j < len(name)-1:
                j+=1
            nm.append([name[i], j-i])
            i = j
        j+=1
        nm.append([name[i], j-i])
        if nm[-1][0] == nm[-2][0]:
            nm[-2][1]+=nm[-1][1]
            nm.pop()
        ty = []
        i = 0
        j = 0
        while j < len(typed)-1:
            j = i+1
            while typed[j]==typed[i] and j < len(typed)-1:
                j+=1
            ty.append([typed[i], j-i])
            i = j
        j+=1
        ty.append([typed[i], j-i])
        if ty[-1][0] == ty[-2][0]:
            ty[-2][1]+=ty[-1][1]
            ty.pop()
        if len(nm)!=len(ty):
            return False
        for i, j in zip(nm, ty):
            if i[0]!=j[0]:
                return False
            if i[1]>j[1]:
                return False
        return True