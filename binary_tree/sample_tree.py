# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Build sample tree for debugging.
root = TreeNode(5)
a = TreeNode(4)
b = TreeNode(11)
c = TreeNode(7)
d = TreeNode(2)
e = TreeNode(8)
f = TreeNode(13)
g = TreeNode(4)
h = TreeNode(1)
root.left = a
root.right = e
a.left = b
b.left = c
b.right = d
e.left = f
e.right = g
g.right = h
