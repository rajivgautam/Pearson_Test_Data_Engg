"""
Question 4.
Imagine you are running a Ponzi scheme. You need to give an explanation, albeit a 
bogus one, to your investors how you made a fortune in the stock market. 
You tell your investors you make money by shorting stock. That is you
make the most money when you sell a stock at a high price and buy it back at
a low price. 
 
Given a list of the daily prices of a stock, calculate the 
maximum profit you can make and which days you would sell and buy the stock. 
For example given a list of prices [4,6,3,5,1,7] you can make a profit of
5 if you sell on day 1 and buy on day 4. Day 1 price = 6, Day 4 price = 1,
profit = 6 - 1 = 5.  Note: You have to sell before you buy. So selling on day
5 and buying on day 4 is impossible. 
Return a tuple in the order of (profit, sell day, buy day). For the above example
the correct return value would be (5, 1, 4).  
"""

def calcProfit(prices):
    
    prices_rev = prices[::-1]  #Given-You have to sell before you buy.
     
    n = len(prices)
    cost = 0
    maxcost = 0
    buy_day = 0
    sell_day = 0 
    min_price = prices_rev[0]
    
    if (n == 0):
        return 0    
 
    for i in range(n):
         
        if min_price > min(min_price, prices_rev[i]):
            min_price = min(min_price, prices_rev[i])
            buy_day = prices.index(prices_rev[i])
                     
        cost = prices_rev[i] - min_price
        
        if maxcost < max(maxcost, cost):            
            maxcost = max(maxcost, cost)
            sell_day = prices.index(prices_rev[i])
                   
    return (maxcost,sell_day,buy_day)


prices = [4,6,3,5,1,7]
print(calcProfit(prices))