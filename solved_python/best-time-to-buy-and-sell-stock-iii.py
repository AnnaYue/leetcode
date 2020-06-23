# Say you have an array for which the i th element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete at most two transactions.

# Note:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
#
# @param prices int整型一维数组
# @return int整型
#
class Solution:
    def maxProfit(self, prices):
        if (not prices):
            return 0
        length = len(prices)
        leftMaxProfit = [0] * length
        rightMaxProfit = [0] * (length+1)

        leftMin = prices[0]
        for i in range(1, length):
            leftMaxProfit[i] = max(leftMaxProfit[i-1], prices[i]-leftMin)
            leftMin = min(leftMin, prices[i])

        rightMax = prices[length-1]
        for i in range(length-2, 0, -1):
            rightMaxProfit[i] = max(
                rightMaxProfit[i+1], rightMax - prices[i])
            rightMax = max(rightMax, prices[i])

        maxProfit = 0
        for i in range(length):
            maxProfit = max(maxProfit, leftMaxProfit[i] + rightMaxProfit[i+1])
        return maxProfit


print(Solution().maxProfit([1, 2, 1, 2, 1, 4]))
