from sample_tree import root


def hasPathSum(root, sum) -> bool:
    if root == None:
        return False

    sum -= root.val

    # Reach a leaf
    if root.left == None and root.right == None:
        return sum == 0
    # Returns true if either left or right child satisfies condition.
    return hasPathSum(root.left, sum) or hasPathSum(root.right, sum)


print(hasPathSum(root, 22))
