from sample_tree import root


# def bfs(root):
#     """Traverse each level."""
#     queue, result = [root, ], []

#     while queue:
#         queue_length = len(queue)
#         # Process this level.
#         for _ in range(queue_length):
#             temp = queue.pop(0)
#             result.append(temp.val)
#             if temp.left != None:
#                 queue.append(temp.left)
#             if temp.right != None:
#                 queue.append(temp.right)

#     return result


# print(bfs(root))

def bfs(root):
    """Keep track of levels."""
    queue, result, levels = [root, ], [], 0

    while queue:
        result.append([])
        # Number of nodes on this level.
        queue_length = len(queue)
        # Process this level.
        for _ in range(queue_length):
            temp = queue.pop(0)
            result[levels].append(temp.val)
            if temp.left != None:
                queue.append(temp.left)
            if temp.right != None:
                queue.append(temp.right)

        levels += 1

    return result


print(bfs(root))
