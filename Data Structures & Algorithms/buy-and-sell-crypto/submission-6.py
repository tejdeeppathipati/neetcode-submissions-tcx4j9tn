class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0,0
        profit = 0
        # left point stays at the same place, 
        #only moves if the left place is less than the right value. 
        #if the right is greater than the proft
        while right < len(prices):
            profit = max(profit, (prices[right] - prices[left]))
            if prices[right] < prices[left]:
                left = right
            right += 1
        return profit