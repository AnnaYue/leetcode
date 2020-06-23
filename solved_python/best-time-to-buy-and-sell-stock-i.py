# Say you have an array for which the i th element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock),
# design an algorithm to find the maximum profit.
# [1,4,2] => 3
# @param prices int整型一维数组
# @return int整型
#
class Solution:
    def maxProfit(self, prices):
        length = len(prices)
        maxProfit = 0
        for i in range(length):
            for j in range(0, i):
                maxProfit = max(prices[i]-prices[j], maxProfit)
        return maxProfit


print(Solution().maxProfit([1, 4, 2]))
