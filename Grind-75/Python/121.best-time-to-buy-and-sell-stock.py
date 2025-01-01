# @leet start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = float('inf')
        for num in prices:

            if num < minPrice:
                minPrice = num
            elif num - minPrice > maxProfit:
                maxProfit = num - minPrice
        return maxProfit

# @leet end
