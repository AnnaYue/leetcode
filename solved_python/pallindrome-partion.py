#
# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return all possible palindrome partitioning of s.

# For example, given s = "aab",
# Return

# [↵    ["aa", "b"], ↵    ["a", "a", "b"]↵]↵
# @param s string字符串
# @return string字符串二维数组
#


class Solution:
    def partition(self, s):
        res = []
        temp = [State([], 0)]
        strLen = len(s)
        while(temp):
            tempState = temp.pop()
            for i in range(tempState.length+1, strLen+1):
                tempStr = s[tempState.length: i]
                if (self.isPallindrome(tempStr)):
                    tempLen = i
                    tempList = tempState.palinList.copy()
                    tempList.append(tempStr)
                    if (tempLen == strLen):
                        res.insert(0, tempList)
                    else:
                        temp.append(State(tempList, tempLen))
        return res

    def isPallindrome(self, s):
        length = len(s)
        if(length == 1):
            return True
        for i in range(length//2):
            if s[i] != s[length-1-i]:
                return False
        return True


class State:
    palinList = []
    length = 0

    def __init__(self, palinList, length):
        self.palinList = palinList
        self.length = length


print(Solution().partition("aab"))
