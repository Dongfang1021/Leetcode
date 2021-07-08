class Solution:
    
    def __init__(self):
        self.mat = 0
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        self.mat = mat
        m = len(mat)
        n = len(mat[0])
        i, j = 0, 0
        while i < m:
            while j < n:
                if (self.mat_val(i, j-1)<self.mat_val(i, j)
                    and self.mat_val(i, j)>self.mat_val(i, j+1)
                    and self.mat_val(i, j)>self.mat_val(i-1, j)
                    and self.mat_val(i, j)>self.mat_val(i+1, j)):
                    return [i, j]
                # left
                elif self.mat_val(i, j) < self.mat_val(i, j-1):
                    j = j-1
                # right
                elif self.mat_val(i, j) < self.mat_val(i, j+1):
                    j = j+1
                # top
                elif self.mat_val(i, j) < self.mat_val(i-1, j):
                    i = i-1
                # bottom
                elif self.mat_val(i, j) < self.mat_val(i+1, j):
                    i = i + 1
                
                
                
    def mat_val(self, i, j) -> int:
        m, n = len(self.mat), len(self.mat[0])
        if i<0 or j<0 or i>=m or j>=n:
            return -1
        else:
            return self.mat[i][j]