from sample_tree import root


def inorderTraversal(root):
    """left -> root -> right, DFS"""
    if root == None:
        return []

    stack, result, curr = [], [], root

    while stack or curr != None:
        # Push left nodes.
        while curr != None:
            stack.append(curr)
            curr = curr.left

        # Nodes in stack already traversed left.
        curr = stack.pop()
        result.append(curr.val)
        curr = curr.right

    return result


print(inorderTraversal(root))


# def inorderTraversal(self, root: TreeNode) -> List[int]:
#     """Recursive solution"""
#     if root == None:
#         return []

#     result = []
#     self.dfs(root, result)
#     return result


# def dfs(self, root, result):
#     if root:
#         self.dfs(root.left, result)
#         result.append(root.val)
#         self.dfs(root.right, result)
