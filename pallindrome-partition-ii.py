#
# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return the minimum cuts needed for a palindrome partitioning of s.

# For example, given s ="aab",
# Return1since the palindrome partitioning["aa","b"]could be produced using 1 cut.

# 示例1
# 输入
# 复制
# "aab"
# 输出
# 复制
# 1
#
# @param s string字符串
# @return int整型
#

class Solution:
    def minCut(self, s):
        res = []
        strLen = len(s)
        cutCount = [-1] + list(range(strLen))
        for i in range(1, strLen):
            for j in range(0, i+1):
                if (self.isPallindrome(s[j:i+1])):
                    cutCount[i+1] = min(cutCount[i+1], cutCount[j]+1)
        return cutCount[strLen]

    def isPallindrome(self, s):
        length = len(s)
        if(length == 1):
            return True
        for i in range(length//2):
            if s[i] != s[length-1-i]:
                return False
        return True


print(Solution().minCut("aab"))
