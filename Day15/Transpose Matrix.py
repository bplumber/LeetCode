class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        lt = []
        for i in range(len(matrix[0])):
            lt.append([])
        for i in matrix:
            for j in range(len(i)):
                lt[j].append(i[j])
        return lt

#ALTERNATE SOLUTION

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        mat = []
        for col in zip(*matrix):
            mat.append(list(col))
        return mat