# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def dfs(node, targetSum, runningSum):
    if node == None:
        return False
    if node.left == None == node.right:     # leaf node
        return runningSum + node.val == targetSum
    return dfs(node.left, targetSum, runningSum + node.val) or dfs(node.right, targetSum, runningSum + node.val)

class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        return dfs(root, targetSum, 0)