from sample_tree import root


# def hasPathSum(root, sum) -> bool:
#     if root == None:
#         return False

#     sum -= root.val

#     # Reach a leaf
#     if root.left == None and root.right == None:
#         return sum == 0
#     # Returns true if either left or right child satisfies condition.
#     return hasPathSum(root.left, sum) or hasPathSum(root.right, sum)


# print(hasPathSum(root, 22))


def hasPathSum(root, sum) -> bool:
    """Iterative solution"""
    if root == None:
        return False

    stack = [(sum, root), ]

    while stack:
        current_sum, node = stack.pop()
        current_sum -= node.val
        if current_sum == 0 and node.left == None and node.right == None:
            return True
        if node.right != None:
            # Store current sum so you can backtrack when you pop this element.
            stack.append((current_sum, node.right))
        if node.left != None:
            stack.append((current_sum, node.left))

    return False


print(hasPathSum(root, 22))
