from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        
        return max_profit

# Example usage:
solution = Solution()
prices1 = [10, 1, 5, 6, 7, 1]
prices2 = [10, 8, 7, 5, 2]

print(solution.maxProfit(prices1))  # Expected output: 6
print(solution.maxProfit(prices2))  # Expected output: 0