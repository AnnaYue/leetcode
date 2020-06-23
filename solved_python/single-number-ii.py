#
# 现在有一个整数类型的数组，数组中只有一个元素只出现一次，其余元素都出现三次。你需要找出只出现一次的元素
# 注意：
# 你需要给出一个线性时间复杂度的算法，你能在不使用额外内存空间的情况下解决这个问题么？
# @param A int整型一维数组
# @return int整型
#
class Solution:
    def singleNumber(self, A):
        bitCount = [0]*65
        for i in A:
            if i < 0:
                bitCount[0] += 1
                i = -i
            bit = 1
            while(i > 0):
                bitCount[bit] += i % 2
                i = i >> 1
                bit += 1

        res = 0
        tempBit = 0
        for i in range(1, len(bitCount)):
            if (bitCount[i] % 3 == 1):
                res += 1 << (i-1)
        if (bitCount[0] % 3 == 1):
            res = -res
        return res


print(Solution().singleNumber([1, 1, 1, 2, 2, 2, -3]))
