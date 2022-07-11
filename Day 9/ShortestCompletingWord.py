class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        plate = ''.join(i for i in licensePlate if not i.isdigit())
        plate = plate.lower()
        plate = plate.replace(" ", "")
        mn = 1000
        output = ""
        for j in words:
            x = j
            count = 0
            for i in plate:
                if i in j:
                    j = j.replace(i, "", 1)
                    count+=1
            if count==len(plate):
                if len(x)<mn:
                    mn = len(x)
                    output = x
            count = 0
        return output