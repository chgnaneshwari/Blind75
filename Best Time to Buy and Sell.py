class Solution:
    def maxProfit(self, prices):
        # Initialize variables to track the minimum price and maximum profit
        min_price = float('inf')  # Start with an infinitely high price
        max_profit = 0  # Start with no profit
        
        # Loop through the prices
        for price in prices:
            # Update min_price to the lowest price encountered so far
            min_price = min(min_price, price)
            
            # Calculate the potential profit if we sold at the current price
            profit = price - min_price
            
            # Update max_profit if the current profit is greater
            max_profit = max(max_profit, profit)
        
        return max_profit
