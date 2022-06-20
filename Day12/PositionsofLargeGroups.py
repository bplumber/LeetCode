class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        currentChar, groupStart = "A", 0
        largeGroups = []
        for i, char in enumerate(s + "A"):  
            if char != currentChar:
                if i - groupStart >= 3:
                    largeGroups.append([groupStart, i - 1])
                currentChar, groupStart = char, i
        return largeGroups