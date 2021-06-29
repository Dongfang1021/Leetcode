class Solution:
    def binary_search(self, array, val):
        index = bisect_left(array, val)
        if index != len(array) and array[index] == val:
            return index
        else:
            return -1
    
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        values = mat[0]
        mat.pop(0)
        for i, val in enumerate(values):
            flag = True
            for arr in mat:
                idx = self.binary_search(arr, val)
                if idx == -1:
                    flag = False
                    break
            if flag:
                return val
        return -1
    