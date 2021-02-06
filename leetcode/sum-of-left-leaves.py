# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def dfs(node):
    if node == None:
        return 0
    res = 0
    if node.left != None and node.left.left == None == node.left.right:
        res += node.left.val
    res += dfs(node.right)
    res += dfs(node.left)
    return res

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return dfs(root)