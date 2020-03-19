class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def levelOrder(root):
    if root == None:
        return []

    queue, result, levels = [root], [], 0

    while queue:
        result.append([])
        level_length = len(queue)
        for _ in range(len(queue)):
            temp = queue.pop(0)
            result[levels].append(temp.val)
            if temp.left != None:
                queue.append(temp.left)
            if temp.right != None:
                queue.append(temp.right)

        levels += 1

    return result
