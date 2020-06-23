# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

# For example,
# Given[100, 4, 200, 1, 3, 2],
# The longest consecutive elements sequence is[1, 2, 3, 4]. Return its length:4.

# Your algorithm should run in O(n) complexity.


# 示例1
# 输入
# [100, 4, 200, 1, 3, 2]
# 输出
# 4

# @param num int整型一维数组
# @return int整型
#
class Solution:
    def longestConsecutive(self, num):
        mapCount = {}
        for i in num:
            mapCount[i] = 1
        for i in mapCount.keys():
            tempKey = i
            if (mapCount[tempKey] != -1):
                j = 1
                while(mapCount.get(tempKey + j)):
                    mapCount[tempKey + j] = -1
                    j += 1
                k = 1
                while(mapCount.get(tempKey - k)):
                    mapCount[tempKey - k] = -1
                    k += 1
                mapCount[tempKey] = j + k - 1
        return max(mapCount.values())


print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
