# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
# An example is the root-to-leaf path1->2->3which represents the number123.
# Find the total sum of all root-to-leaf numbers.
# For example,
#     1↵   / ↵  2   3
# The root-to-leaf path1->2represents the number12.
# The root-to-leaf path1->3represents the number13.
# Return the sum = 12 + 13 =25.
#
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#
#
# @param root TreeNode类
# @return int整型
#


class Solution:
    def sumNumbers(self, root):
        if (not root):
            return 0
        root.path = str(root.val)
        iterNode = [root]
        res = 0
        while(iterNode):
            tempNode = iterNode.pop()
            if (tempNode.left):
                leftNode = tempNode.left
                leftNode.path = tempNode.path + str(leftNode.val)
                iterNode.append(leftNode)
            if (tempNode.right):
                rightNode = tempNode.right
                rightNode.path = tempNode.path + str(rightNode.val)
                iterNode.append(rightNode)
            if (not tempNode.left and not tempNode.right):
                res += int(tempNode.path)
        return res


root = TreeNode(1)
left = TreeNode(2)
right = TreeNode(3)
root.left = left
root.right = right
son = TreeNode(4)
left.left = son
print(Solution().sumNumbers(root))
