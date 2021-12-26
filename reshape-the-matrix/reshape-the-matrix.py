class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        A = [x for row in mat for x in row]
        if r*c == len(A):
            return [A[i*c:(i+1)*c] for i in range(r)]
        else:
            return mat
        