from sample_tree import root


def preorderTraversal(root):
    """root -> left -> right, DFS"""
    if root == None:
        return []

    stack, result = [root, ], []

    while stack:
        root = stack.pop()
        result.append(root.val)
        if root.right != None:
            stack.append(root.right)
        # Push left last because LIFO.
        if root.left != None:
            stack.append(root.left)

    return result


print(preorderTraversal(root))


def preorderTraversal(self, root):
    if root == None:
        return []

    result = []
    self.dfs(root, result)
    return result


def dfs(self, root, result):
    if root:
        result.append(root.val)
        self.dfs(root.left, result)
        self.dfs(root.right, result)
