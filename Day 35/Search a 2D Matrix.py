class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        row = -1
        l = 0
        r = len(matrix)-1
        while l<=r:
            mid = (l+r)//2
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                row = mid
                l = 0
                r = len(matrix[row])-1
                while l <= r:
                    mid = (l+r)//2
                    if matrix[row][mid] == target:
                        return True
                    if target > matrix[row][mid]:
                        l = mid+1
                    if target < matrix[row][mid]:
                        r = mid-1
                break
            if target > matrix[mid][-1]:
                l = mid+1
            if target < matrix[mid][0]:
                r = mid-1
        return False