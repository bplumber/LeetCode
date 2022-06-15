class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for i in letters:
            if new[-1]!=i:
                new.append(i)
        new = new[1:] 
        for i in new:
            if ord(i)>ord(target):
                return i
        return new[0]