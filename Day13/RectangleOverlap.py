class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, y1, x2, y2=rec1
        x12,y12,x22,y22=rec2
        if y22 <= y1:
            return False
		if y12 >= y2:
            return False
        if x22 <= x1:
            return False
        if x12 >= x2:
            return False
        return True