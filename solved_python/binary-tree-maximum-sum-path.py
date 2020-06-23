# Given a binary tree, find the maximum path sum.
# The path may start and end at any node in the tree.

# For example:
# Given the below binary tree,

#        1↵      / ↵     2   3↵

# Return6.
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
    def maxPathSum(self, root):
        stack = [root]
        while(stack):
            node = stack.pop()
            if ((not node.left) and (not node.right)):
                node.maxUp = node.val
                node.maxAround = node.val
            else:
                if ((node.left and hasattr(node.left, 'maxUp')) or (node.right and hasattr(node.right, 'maxUp'))):
                    if (node.left):
                        leftUp = node.left.maxUp
                        leftAround = node.left.maxAround
                        if (not node.right):
                            node.maxUp = max(node.val, leftUp + node.val)
                            node.maxAround = max(leftAround, node.maxUp)
                    if (node.right):
                        rightUp = node.right.maxUp
                        rightAround = node.right.maxAround
                        if (not node.left):
                            node.maxUp = max(node.val, rightUp + node.val)
                            node.maxAround = max(rightAround, node.maxUp)
                    if (node.left and node.right):
                        node.maxUp = max(node.val, leftUp +
                                         node.val, rightUp + node.val)
                        node.maxAround = max(
                            leftAround, rightAround, node.maxUp, leftUp + rightUp + node.val)
                else:
                    stack.append(node)
                    if (node.left):
                        stack.append(node.left)
                    if (node.right):
                        stack.append(node.right)
        return root.maxAround


root = TreeNode(1)
left = TreeNode(2)
right = TreeNode(3)
root.left = left
root.right = right
son = TreeNode(4)
left.left = son

print(Solution().maxPathSum(root))
