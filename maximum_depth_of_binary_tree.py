# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        depth = 0
        self.dfs(root.left, depth)
        self.dfs(root.right, depth)
        return depth

    def dfs(self, root, depth):
        if root != None:
            depth += 1
            self.dfs(root.left, depth)
            self.dfs(root.right, depth)
