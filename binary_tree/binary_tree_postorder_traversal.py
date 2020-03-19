from sample_tree import root


def postorderTraversal(root):
    """left -> right -> root, DFS"""
    if root == None:
        return []

    stack, result = [root, ], []

    # Do root -> right -> left then reverse.
    while stack:
        root = stack.pop()
        result.append(root.val)
        if root.left != None:
            stack.append(root.left)
        if root.right != None:
            stack.append(root.right)

    return result[::-1]


print(postorderTraversal(root))

# def postorderTraversal(root):
#     """recursive solution"""
#     if root == None:
#         return []

#     result = []
#     self.dfs(root, result)
#     return result


# def dfs(self, root, result):
#     if root:
#         self.dfs(root.left, result)
#         self.dfs(root.right, result)
#         result.append(root.val)
