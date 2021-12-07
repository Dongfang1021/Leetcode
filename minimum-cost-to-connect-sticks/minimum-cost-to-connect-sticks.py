class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        minCost = 0
        heapq.heapify(sticks)
        while len(sticks) > 1:
            cost = heapq.heappop(sticks) + heapq.heappop(sticks)
            heapq.heappush(sticks, cost)
            minCost += cost
        return minCost
    