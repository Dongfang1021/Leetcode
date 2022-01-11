class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bought, sold = float('-inf'), 0
        for p in prices:
            bought, sold = max(bought, -p), max(sold, bought+p)
        return sold
        