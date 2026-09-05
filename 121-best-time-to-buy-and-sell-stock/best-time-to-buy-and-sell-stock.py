class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=prices[0]
        max_profit=float('-inf')
        for i in prices:
            min_price=min(i,min_price)
            max_profit=max(max_profit,i-min_price)
        return max_profit