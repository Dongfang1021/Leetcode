class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        store = []
        for i, val in enumerate(mat):
            store.append([i, sum(val)])
        store.sort(key = lambda x: x[1])
        return [store[i][0] for i in range(k)]
        
    

    