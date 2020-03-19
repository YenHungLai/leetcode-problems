"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root == None:
            return 0

        stack, depth = [(1, root)], 0

        while stack:
            curr_depth, root = stack.pop()
            depth = max(curr_depth, depth)
            if root.children != None:
                for child in root.children:
                    stack.append((curr_depth + 1, child))

        return depth


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        """Recursive solution"""
