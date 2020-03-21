from sample_tree import root


def find_all_path(root):
    path = []
    dfs(root, path)


def dfs(root, path):
    # Do not modify original list.
    temp = path.copy()
    temp.append(root.val)
    # Reached a left.
    if root.left == None and root.right == None:
        return print(temp)
    if root.left != None:
        dfs(root.left, temp)
    if root.right != None:
        dfs(root.right, temp)


print(find_all_path(root))
