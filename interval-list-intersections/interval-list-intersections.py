class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        intersection = []
        i, j = 0, 0
        while i < len(firstList) and j < len(secondList):
            if secondList[j][1] >= firstList[i][0]:
                start = max(firstList[i][0], secondList[j][0])
                end = min(firstList[i][1], secondList[j][1])
                if start <= end:
                    intersection.append([start, end])
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return intersection
        
    
        