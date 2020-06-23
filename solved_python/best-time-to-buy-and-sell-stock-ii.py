# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit.
# You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times).
# However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
#
# @param prices int整型一维数组
# @return int整型
#
class Solution:
    def maxProfit(self, prices):
        length = len(prices)
        sumProfit = 0
        periodProfit = 0
        for i in range(1, length):
            tempProfit = prices[i] - prices[i-1]
            if (tempProfit > 0):
                periodProfit += tempProfit
            else:
                sumProfit += periodProfit
                periodProfit = 0
        sumProfit += periodProfit
        return sumProfit


print(Solution().maxProfit([1, 0, 1]))
