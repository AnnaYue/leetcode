# Given an index k, return the k th row of the Pascal's triangle.
# For example, given k = 3,
# Return[1,3,3,1].

# Note:
# Could you optimize your algorithm to use only O(k) extra space?
# @param rowIndex int整型
# @return int整型一维数组
#
class Solution:
    def getRow(self, rowIndex):
        res = [1]
        for i in range(1, rowIndex+1):
            res.append(res[i-1]*(rowIndex - i + 1)//i)
        return res


print(Solution().getRow(5))
