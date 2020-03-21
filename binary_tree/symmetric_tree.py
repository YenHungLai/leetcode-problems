from sample_tree import root


def isSymmetric(root):
    """Traverse left and right subtree in oppsite direction"""
    stack_left = []
    stack_right = []
    dfs_left(root.left, stack_left)
    dfs_right(root.right, stack_right)
    print(stack_left, stack_right)


def dfs_left(root, stack):
    if root:
        stack.append(root.val)
        dfs_left(root.left, stack)
        dfs_left(root.right, stack)


def dfs_right(root, stack):
    if root:
        stack.append(root.val)
        dfs_right(root.right, stack)
        dfs_right(root.left, stack)


isSymmetric(root)
