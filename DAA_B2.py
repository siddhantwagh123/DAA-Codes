'''Implement a problem of maximize Profit by trading stocks based on given rate per day.

Statement: Given an array arr[] of N positive integers which denotes the cost of selling and buying a stock on each of the N days. 
The task is to find the maximum profit that can be earned by buying a stock on or selling all previously bought stocks on a particular day.'''

def maxProfit(prices):
    if len(prices) < 2:
        return 0
    #Initialize the minimum price and maximum profit
    min_price = prices[0]
    max_profit = 0
    
    #Iterate through the list of prices
    for price in prices:
        #Update the minimum price if the current price is lower
        if price < min_price:
            min_price = price
        
        #Calculate the profit if the current price is sold at this point
        profit = price - min_price
        
        #Update the maximum profit if the current profit is greater than previous maximum profit
        if profit > max_profit:
            max_profit = profit
    
    return max_profit

prices = [2,3,5]
print("Maximum Profit:", maxProfit(prices))
