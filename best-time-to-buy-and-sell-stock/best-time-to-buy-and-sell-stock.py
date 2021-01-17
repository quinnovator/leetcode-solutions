class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Check if the list of prices is empty or not
        if not prices:
            return 0
        
        currentLow = 0
        profit = 0
        
        # Constantly updates index of lowest element, updates profit with each pass
        x = 1
        while x < len(prices):
            if prices[x] - prices[currentLow] > profit:
                profit = prices[x] - prices[currentLow]
            elif prices[x] < prices[currentLow]:
                currentLow = x
            x += 1
        
        return(profit)
