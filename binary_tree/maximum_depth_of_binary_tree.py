# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """Recursive"""
        if root is None:
            return 0
        else:
            # depth(root) = max(depth(left), depth(right))
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1


def maxDepth(self, root):
    if root == None:
        return 0

    # Push current depth into stack.
    stack, result = [(1, root)], 0

    while stack:
        current_depth, root = stack.pop()
        result = max(result, current_depth)
        # Push all its children and their depth to stack.
        if root.left != None:
            stack.append((current_depth + 1, root.left))
        if root.right != None:
            stack.append((current_depth + 1, root.right))

    return result
