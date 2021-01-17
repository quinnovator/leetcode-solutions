class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Min val only matters at each point of the list, not retroactive
        minVal = float('inf')
        maxProfit = 0
        
        for x in range(len(prices)):
            if (prices[x] < minVal):
                minVal = prices[x]
            elif (prices[x] - minVal > maxProfit):
                maxProfit = prices[x] - minVal
                
        return maxProfit
