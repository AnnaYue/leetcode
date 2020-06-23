#
# Given numRows, generate the first numRows of Pascal's triangle.
# For example, given numRows = 5,
# Return

# [↵     [1],↵    [1,1],↵   [1,2,1],↵  [1,3,3,1],↵ [1,4,6,4,1]↵]
# @param numRows int整型
# @return int整型二维数组
#
class Solution:
    def generate(self, numRows):
        if (numRows <= 0):
            return []
        parent = [1]
        pascalTriangle = [parent]
        for i in range(numRows-1):
            current = [1]
            for j in range(i):
                current.append(parent[j] + parent[j+1])
            current.append(1)
            pascalTriangle.append(current)
            parent = current
        return pascalTriangle


print(Solution().generate(5))
