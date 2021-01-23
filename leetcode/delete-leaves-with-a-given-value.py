# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# dfs(node) returns a TreeNode such that no leaf has value target
def dfs(node, target):
    if node.left == None == node.right:     # base case of leaf
        if node.val == target:
            return None
        else:
            return node
    if node.left != None:
        left_node = dfs(node.left, target)
    else:
        left_node = None
    if node.right != None:
        right_node = dfs(node.right, target)
    else:
        right_node = None
    node.left = left_node
    node.right = right_node
    if node.left == None and node.right == None:
        if node.val == target:
            return None
    return node


class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        return dfs(root, target)