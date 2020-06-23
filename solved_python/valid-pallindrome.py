#
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# For example,
# "A man, a plan, a canal: Panama"is a palindrome.
# "race a car"is not a palindrome.

# Note:
# Have you consider that the string might be empty? This is a good question to ask during an interview.

# For the purpose of this problem, we define empty string as valid palindrome.
# @param s string字符串
# @return bool布尔型
#
class Solution:
    def isPalindrome(self, s):
        if (not s):
            return True
        s = s.rstrip().lstrip().lower()
        length = len(s)
        if(length == 1):
            return True
        i = 0
        j = length-1
        while(j >= i):
            while(i < j and not self.isLetter(s[i])):
                i += 1
            while(i < j and not self.isLetter(s[j])):
                j -= 1
            if (s[i] != s[j]):
                return False
            i += 1
            j -= 1
        return True

    def isLetter(self, c):
        return (c >= 'a' and c <= 'z') or (c >= '0' and c <= '9')


print(Solution().isPalindrome(",,,,,"))
