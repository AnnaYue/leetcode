# There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1).
# You begin the journey with an empty tank at one of the gas stations.
# # Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

# Note:
# The solution is guaranteed to be unique.

# 示例1
# 输入
# [2,3,1],[3,1,2]
# 复制
# 1
#
# @param gas int整型一维数组
# @param cost int整型一维数组
# @return int整型
#
class Solution:
    def canCompleteCircuit(self, gas, cost):
        length = len(gas)
        minus = [0]*length
        sumGas = 0
        sumCost = 0
        for i in range(length):
            minus[i] = gas[i] - cost[i]
            sumGas += gas[i]
            sumCost += cost[i]
        if (sumGas < sumCost):
            return -1
        maxStart = self.maxStart(minus + minus)
        return maxStart

    def maxStart(self, list):
        length = len(list)
        maxStart = 0
        maxSum = 0
        currentStart = 0
        currentSum = 0
        for i in range(0, length):
            if (list[i] > 0):
                currentSum += list[i]
                if (currentSum > maxSum):
                    maxSum = currentSum
                    maxStart = currentStart
            else:
                currentSum += list[i]
                if (currentSum < 0):
                    while(list[i] <= 0):
                        i += 1
                    currentStart = i
                    currentSum = list[i]
        return maxStart


print(Solution().canCompleteCircuit([1, 0, 0], [0, 0, 1]))
