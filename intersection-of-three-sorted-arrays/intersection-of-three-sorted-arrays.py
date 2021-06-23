class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        return (Counter(arr1) & Counter(arr2) & Counter(arr3)).elements()
        