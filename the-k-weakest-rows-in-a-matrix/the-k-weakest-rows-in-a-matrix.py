class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        indexes = []
        for c, r in itertools.product(range(n), range(m)):
            if len(indexes) == k:
                break
            if mat[r][c] == 0 and (c == 0 or mat[r][c - 1] == 1):
                indexes.append(r)
        i = 0
        while len(indexes) < k:
            if mat[i][-1] == 1:
                indexes.append(i)
            i += 1
        return indexes
    