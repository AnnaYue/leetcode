#
# 求给定的二叉树的前序遍历。
# 例如：
# 给定的二叉树为{1,#,2,3},
#    1↵    ↵     2↵    /↵   3↵
# 返回：[1,2,3].
# 备注；用递归来解这道题太没有新意了，可以给出迭代的解法么？
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#
#
# @param root TreeNode类
# @return int整型一维数组
#


class Solution:
    def preorderTraversal(self, root):
        treeList = [root]
        res = []
        if (root == None):
            return res
        while(len(treeList) > 0):
            currentNode = treeList.pop()
            res.append(currentNode.val)
            if (currentNode.right):
                treeList.append(currentNode.right)
            if (currentNode.left != None):
                treeList.append(currentNode.left)
        return res


root = TreeNode(1)
right = TreeNode(2)
right.left = TreeNode(3)
root.right = right
print(Solution().preorderTraversal(root))
