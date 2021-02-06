# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def dfs(node):  # dfs(node) returns min depth of subtree rooted at node
    if node == None:
        return 0
    
    if node.left == None == node.right:
        return 1
    if node.left and node.right:
        return min(dfs(node.left), dfs(node.right)) + 1
    elif node.left:
        return dfs(node.left) + 1
    else:
        return dfs(node.right) + 1

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return dfs(root)