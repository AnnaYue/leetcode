#
# There are N children standing in a line. Each child is assigned a rating value.
# You are giving candies to these children subjected to the following requirements:

# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# What is the minimum candies you must give?

# 示例1
# 输入
# 复制
# [1,2,2]
# 输出
# 复制
# 4
# @param ratings int整型一维数组
# @return int整型
#
class Solution:
    def candy(self, ratings):
        length = len(ratings)
        candies = [1]*length
        increaseList = self.maxLongestIncrease(ratings)
        ratings.reverse()
        decreaseList = self.maxLongestIncrease(ratings)
        decreaseList.reverse()
        res = 0
        for i in range(length):
            res += max(increaseList[i], decreaseList[i])
        return res

    def maxLongestIncrease(self, list):
        length = len(list)
        res = [1]*length
        for i in range(1, length):
            if list[i] > list[i-1]:
                res[i] = res[i-1] + 1
        return res


print(Solution().candy([1, 2, 2]))
